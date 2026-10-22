#Cap funksiyasi
# 1.+ isaresi ile 
ad="Fidan"
soyad="Yusifova"
yash=18

print(ad+soyad) # run edende bitisik sekilde FidanYusifova cixir 

print(ad+" "+soyad) # bele run edende ise Fidan Yusifova cixir  yeni ki dirnaq qoyub icinede bosluq qoysaq ayri ayri olucaq 

print("ad: " +ad+" "+"soyad: " +soyad +yash ) #bele yazanda eror verecek cunki burda biri int tipinde qalanlari str tipinde olanda 
# ona gorede yash yazilisinda sehvlik car onun evezine asagidaki duzgun formada yaz
print("ad: " +ad+" "+"soyad : " +soyad + " " str (yash)) # bele formada yazsan daha duzgun olacaq ve onlar arasinda bosluq olur  onuda nece elemek olar 
# " " bele yazanda bosluq olur aralarinda 

print("ad: " +ad+" "+"soyad: " +soyad + "yash: " str (yash)) # bele formada da yazmaq olar 

# + bir ayirici vasitesi kimi istifade edirik 
 
# 2. , vergulle ayirmaq 
print("ad; ",) # bele bosluq qiymaga ehtiyac yoxdu cunki vergul ozu bosluq rolunu oynayir oz ozunde bosluq qoyur 

print ("ad: ",ad," ","soyad: ",soyad,"yash: ",yash) he bide ki burda + deki kimi str ehtiyac yoxdu yazmaga , vergel ozu hell edir str tipi edir yeni.
