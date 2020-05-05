var phone_number="01048379834"
var len=phone_number.length
var plist=phone_number.split("")
for(var i=0;i<len-4;i++)
    {
        plist.shift()
    }
for(var i=0;i<len-4;i++)
    {
        plist.unshift("*")
    }
console.log(plist.join(""))
