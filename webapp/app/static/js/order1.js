function showDescription() {
  var selectBox = document.getElementById("category");
  var selectedValue = selectBox.options[selectBox.selectedIndex].value;
  var materialSelectBox = document.getElementById("material");
  var selectedMaterial = materialSelectBox.options[materialSelectBox.selectedIndex].value;
  var sizeDescription = document.getElementById("size_description");
  var materialDescription = document.getElementById("material_description");

  if (selectedValue === "A0") {
      sizeDescription.innerHTML = "ขนาดป้าย ไวนิล (841 x 1189 มิลลิเมตร) ใช้สำหรับการสร้างป้ายโฆษณาหรือป้ายประชาสัมพันธ์ขนาดใหญ่ในสถานที่สาธารณะ";
  } else if (selectedValue === "A1") {
      sizeDescription.innerHTML = "ขนาดป้าย ไวนิล (594 x 841 มิลลิเมตร) ใช้สำหรับการสร้างป้ายโฆษณาหรือป้ายประชาสัมพันธ์ขนาดกลาง";
  } else if (selectedValue === "A2") {
      sizeDescription.innerHTML = "ขนาดป้าย ไวนิล (420 x 594 มิลลิเมตร) ใช้สำหรับการสร้างป้ายโฆษณาหรือป้ายประชาสัมพันธ์ขนาดเล็กถึงกลาง";
  } else if (selectedValue === "A3") {
      sizeDescription.innerHTML = "ขนาดป้าย ไวนิล (297 x 420 มิลลิเมตร) ใช้สำหรับการสร้างป้ายสำหรับงานประชุมหรืองานอีเวนต์";
  } else if (selectedValue === "A4") {
      sizeDescription.innerHTML = "ขนาดป้าย ไวนิล (210 x 297 มิลลิเมตร) ใช้สำหรับการสร้างป้ายประชาสัมพันธ์หรือป้ายโฆษณาขนาดเล็ก";
  }

  if (selectedMaterial === "Vinyl") {
      materialDescription.innerHTML = "ป้ายไวนิลธงญี่ปุ่น ซึ่งป้ายปริ้นอิงค์เจ็ทขนาดเล็กที่ใช้ในการโฆษณา สามารถวางตั้งบริเวณหน้าร้านได้ เป็นป้ายที่สามารถมองเห็นได้ทั้ง 2 ด้าน มีน้ำหนักเบา เคลื่อนย้ายตำแหน่งที่วางได้สะดวก";
  } else if (selectedMaterial === "Acrylic") {
      materialDescription.innerHTML = "ป้ายไวนิลโครงไม้และโครงเหล็ก โดยเป็นการนำป้ายไวนิลปริ้นอิงค์เจ็ทมาประยุกต์ใช้ยึดติดกับโครงไม้หรือโครงเหล็ก เพื่อความสวยงามเพราะการขึงโครงจะทำให้ไวนิลไม่สะบัด ทำให้ป้ายเด่นชัดยิ่งขึ้น";
  } else if (selectedMaterial === "Metal") {
      materialDescription.innerHTML = "ป้ายไวนิลกล่องไฟ โดยเป็นการนำไวนิลชนิดพิเศษมาประยุกต์ใช้ในการประกอบเป็นตู้ไฟ โดยใช้ไวนิลชนิดโปร่งแสงในการผลิต";
  } else if (selectedMaterial === "Wood") {
      materialDescription.innerHTML = "สติกเกอร์อิงค์เจ็ท เป็นสติกเกอร์ที่มีความคมชัด พิมลวดลายได้อย่างอิสระ มีความทนทาน สีสันสวยงาม สามารถนำไปประยุกต์ใช้งานได้หลายรูปแบบ";
  } else if (selectedMaterial === "Foamboard") {
      materialDescription.innerHTML = "แคนวาสอิงค์เจ็ท เป็นการพิมพ์ลงบนผ้าแคนวาส ให้งานที่ออกมาสวยงาม นิยมใช้เป็นภาพกรอบลอย ตกแต่งงานมงคล หรือให้เป็นของขวัญใน";
  }
}
