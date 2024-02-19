function populateOptions() {
    // เริ่มต้นตัวเลือกของวัน
    var daySelect = document.getElementById("day");
    for (var i = 1; i <= 31; i++) {
        var option = document.createElement("option");
        option.value = i < 10 ? "0" + i : i.toString();
        option.text = i < 10 ? "0" + i : i.toString();
        daySelect.add(option);
    }

    // เริ่มต้นตัวเลือกของเดือน
    var monthSelect = document.getElementById("month");
    var months = ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"];
    for (var i = 0; i < months.length; i++) {
        var option = document.createElement("option");
        option.value = i < 9 ? "0" + (i + 1) : (i + 1).toString();
        option.text = months[i];
        monthSelect.add(option);
    }

    // เริ่มต้นตัวเลือกของปี
    var yearSelect = document.getElementById("year");
    var currentYear = new Date().getFullYear();
    for (var i = currentYear; i >= currentYear - 100; i--) {
        var option = document.createElement("option");
        option.value = i.toString();
        option.text = i.toString();
        yearSelect.add(option);
    }
}

window.onload = populateOptions;

function submitForm() {
    var selectedDay = document.getElementById("day").value;
    var selectedMonth = document.getElementById("month").value;
    var selectedYear = document.getElementById("year").value;

    alert("วันที่คุณเลือก: " + selectedDay + "/" + selectedMonth + "/" + selectedYear);
}