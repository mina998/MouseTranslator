#Requires AutoHotkey v2.0
mkey := FileRead("mkey")
If (mkey == "XButton1"){
    XButton1:: Send "^\"
}
If (mkey == "XButton2"){
    XButton2:: Send "^\"
}
If (mkey == "MButton"){
    MButton:: Send "^\"
}
