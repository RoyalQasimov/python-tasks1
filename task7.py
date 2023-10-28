a = []
max_a_list = 15
a = input("ad daxil edin")
if len(a) > max_a_list :
    print("error: bu ad cox uzundu,15 herfden artig olmaz") 
elif a == "" :
    print("error: ad daxil edilmeyib")
else:
    print("ad ugurla elave edilib")