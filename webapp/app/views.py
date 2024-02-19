import datetime
from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect , JsonResponse
from django.template import RequestContext
from django.db import IntegrityError
from .models import *
from .forms import *
from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.contrib import messages
from .models import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db import transaction
from django.utils import timezone
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST


def home(req):
    return render(req,'app/home.html')


def registerXlogin(req):
    return render(req,'app/login.html')


def signout(request):
    logout(request)
    return redirect('home')

@login_required
def admin_order_list(request):
    orders = Order.objects.all()
    return render(request, 'admin/order_list.html', {'orders': orders})


def update_order_status(request, order_id):
    if request.method == 'POST':
        new_status = request.POST.get('status')
        order = get_object_or_404(Order, id=order_id)
        order.status = new_status
        order.save()
        messages.success(request, 'อัพเดทสถานะคำสั่งซื้อเรียบร้อยแล้ว')
        return redirect('admin_order_list')
    else:
        messages.error(request, 'การอัพเดทสถานะคำสั่งซื้อล้มเหลว')
        return redirect('admin_order_list')

def view_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'admin/view_order.html', {'order': order})

@login_required
def track_order(request, order_id):
    if hasattr(request.user, 'userprofile'):
        order = get_object_or_404(Order, id=order_id, user_profile=request.user.userprofile)
        order_status = order.get_status_display()
        return render(request, 'productweb/track_order.html', {'order': order, 'order_status': order_status})
    else:
        return render(request, 'app/no_profile.html')



def admin1(request):
    orders = Order.objects.all()
    return render(request, 'admin/admin1.html', {'orders': orders})


def management(request):
    return render(request, 'admin/management.html', {'user': request.user})


def user_management_view(request):
    user_profiles = UserProfile.objects.all()
    return render(request, 'admin/management.html', {'user_profiles': user_profiles})


def register(req):
    if req.method == "POST":
        username = req.POST['username']
        fname = req.POST['fname']
        lname = req.POST['lname']
        email = req.POST['email']
        pass1 = req.POST['pass1']

        if User.objects.filter(username=username).exists():
            messages.error(req, "Username is already taken. Please choose a different username.")
            return render(req, "app/register.html")

        try:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()

            UserProfile.objects.create(user=myuser, first_name=fname, last_name=lname, email=email, pass1=pass1)
            messages.success(req, "สร้างบัญชีเรียบร้อย ")
            return redirect('login')

        except IntegrityError:
            messages.error(req, "An error occurred while creating the user. Please try again.")
            return render(req, "app/register.html")

    return render(req, "app/register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "เข้าสู่ระบบสำเร็จ")

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'เข้าสู่ระบบสำเร็จ'})
            else:
                return redirect('home')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'ข้อมูลเข้าสู่ระบบไม่ถูกต้อง'})
            else:
                messages.error(request, "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
                return redirect('login')

    return render(request, 'app/login.html')


@login_required
def edit_profile(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            day = request.POST.get('day')
            month = request.POST.get('month')
            year = request.POST.get('year')
            birth_date_str = f"{year}-{month}-{day}"
            birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
            user_profile.birth_date = birth_date
            user_profile.save()
            messages.success(request, 'บันทึกข้อมูลเรียบร้อยแล้ว')
            return redirect('profile')
        else:
            messages.error(request, 'กรุณากรอกข้อมูลที่ถูกต้อง')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'app/edit_profile.html', {'form': form})


@login_required
def upload_profile_image(request):
    if request.method == 'POST':
        profile_image = request.FILES.get('profile_image')
        if profile_image:
            request.user.userprofile.profile_image = profile_image
            request.user.userprofile.save()
            messages.success(request, 'อัพโหลดโปรไฟล์เรียบร้อยแล้ว')
        else:
            messages.error(request, 'กรุณาเลือกรูปภาพ')
    return redirect('profile')


@login_required
def profile(request):
    return render(request, 'app/profile.html', {'user': request.user})

def products(request):
    all_products = Item.objects.all()
    context = {'products': all_products}
    return render(request, 'productweb/product.html', context)


def product(request, item_id):
    item_instance = get_object_or_404(Item, id=item_id)
    return render(request, 'productweb/product_detail.html', {'item': item_instance})

def add_product(request):
    if request.method == 'POST':
        item_form = ItemForm(request.POST)
        image_form = ItemImageForm(request.POST, request.FILES)

        if item_form.is_valid() and image_form.is_valid():
            item = item_form.save()
            image = image_form.save(commit=False)
            image.item = item
            image.save()

            return redirect('products') 
    else:
        item_form = ItemForm()
        image_form = ItemImageForm()

    return render(request, 'productweb/add_product.html', {'item_form': item_form, 'image_form': image_form})

def delete_product(request, product_id):
    product = get_object_or_404(Item, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('products') 

    return render(request, 'productweb/delete_product.html', {'product': product})

@login_required
def cart(req):
    try:
        user_profile = UserProfile.objects.get(user=req.user)
        cart, created = Cart.objects.get_or_create(cart=user_profile)
        
        cart_detail = Detailcart.objects.filter(carts=cart)
        count = sum(detail.amount for detail in cart_detail)
        
        context = {'count': count, 'cart': cart_detail}
        return render(req, 'productweb/cart.html', context)
    except UserProfile.DoesNotExist:
        return render(req, 'app/no_profile.html')

@login_required
def add_cart(req, id):
    products = ItemImage.objects.filter(item=id)
    
    try:
        user_profile = UserProfile.objects.get(user=req.user)
        cart, created = Cart.objects.get_or_create(cart=user_profile)
        product_instance = products.first()
        
        cart_detail = Detailcart.objects.create(
            itemImages=product_instance,
            carts=cart,
            amount=1,
        )
        cart_detail.save()
        return HttpResponseRedirect(reverse('cart'))
    except UserProfile.DoesNotExist:
        pass

def add_products(request, product_id):
    product_instance = Item.objects.get(id=product_id)
    context = {'product': product_instance}
    return render(request, 'productweb/add_products.html', context)
    
def contag(req):
    return render(req,'productweb/contag.html')

def payments(req):
    return render(req,'payment/payments.html')

@login_required
def order(request):
    if request.method == 'POST':
        user_profile = request.user.userprofile  
        name = request.POST.get('name')
        category = request.POST.get('category')
        material = request.POST.get('material')
        message = request.POST.get('message')
        attachment = request.FILES.get('attachment')

        status = 'รอดำเนินการ'

        order = Order.objects.create(
            user_profile=user_profile,
            name=name,
            category=category,
            material=material,
            message=message,
            attachment=attachment,
            status=status 
        )
        try:
            with transaction.atomic():
                cart = Cart.objects.select_for_update().get(cart=user_profile)
                cart_items = Detailcart.objects.filter(carts=cart)
                cart_items.delete()
                messages.success(request, 'Your order has been placed successfully!')
        except Cart.DoesNotExist:
            pass
        return redirect('preorder') 

    return render(request, 'productweb/order.html')


def order2(request):
    return render(request, 'productweb/order2.html')
def order3(request):
    return render(request, 'productweb/order3.html')
def order4(request):
    return render(request, 'productweb/order4.html')
def order5(request):
    return render(request, 'productweb/order5.html')
def order6(request):
    return render(request, 'productweb/order6.html')

@login_required
def preorder(request, order_id=None):
    if order_id:
        return redirect('track_order', order_id=order_id)
    else:
        current_user = request.user
        orders = Order.objects.filter(user_profile__user=current_user).order_by('-created_at')
        return render(request, 'productweb/preorder.html', {'orders': orders})

def delete_product_incart(request, product_id):
    cart_item = get_object_or_404(Detailcart, id=product_id)
    if request.method == 'POST':
        cart_item.delete()
        return redirect('cart') 
    return render(request, 'productweb/delete_product.html', {'product': cart_item})



def delete_product(request, product_id):
    # หากมีการ POST คำขอการลบสินค้า
    if request.method == 'POST':
        # หากต้องการยืนยันการลบสินค้า
        if 'confirm_delete' in request.POST:
            product = get_object_or_404(Item, pk=product_id)
            product.delete()
            return redirect('products')  # ลิงก์กลับไปยังหน้ารายการสินค้าหลัก
        else:
            return redirect('products')  # หากยกเลิกการลบสินค้า กลับไปยังหน้ารายการสินค้า
    else:
        product = get_object_or_404(Item, pk=product_id)
        return render(request, 'productweb/delete_product.html', {'product': product})

########                   ระบบแชท           ################
@login_required
def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:  # ตรวจสอบว่ามีข้อมูล content หรือไม่
            admin_user = User.objects.filter(is_staff=True).first()
            if admin_user:
                admin_id = admin_user.id
                # สร้างข้อความใหม่และบันทึกลงในฐานข้อมูล
                message = Message.objects.create(sender=request.user.userprofile, receiver_id=admin_id, content=content)
                message.save()
                return redirect('chat')
    return redirect('chat')



@login_required
def chat(request):
    # เรียกดูข้อความทั้งหมดที่ผู้ใช้เคยส่งไปและเป็นผู้รับหรือผู้ส่งเอง
    messages = Message.objects.filter(sender=request.user.userprofile) | Message.objects.filter(receiver=request.user.userprofile)
    context = {
        'messages': messages
    }
    return render(request, 'app/chat.html', context)


@login_required
def chat_history(request, receiver_id):
    # เรียกดูประวัติการแชทกับผู้ใช้ที่กำหนด
    messages = Message.objects.filter(sender=request.user.userprofile, receiver_id=receiver_id) | Message.objects.filter(sender_id=receiver_id, receiver=request.user.userprofile)
    context = {
        'messages': messages
    }
    return render(request, 'app/chat_history.html', context)

from django.contrib.auth.models import User

@login_required
def admin_chat(request):
    admin_user = User.objects.get(is_staff=True)
    admin_profile = admin_user.userprofile  # หา UserProfile ของแอดมิน
    # เรียกดูข้อความทั้งหมดที่ผู้ใช้เคยส่งไปและเป็นผู้รับหรือผู้ส่งเอง
    messages = Message.objects.filter(sender=request.user.userprofile, receiver=admin_profile) | \
               Message.objects.filter(sender=admin_profile, receiver=request.user.userprofile)
    context = {
        'messages': messages
    }
    return render(request, 'app/admin_chat.html', context)


########                   ระบบแชท           ################