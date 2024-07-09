num_to_word={
    1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'7', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'70', 80:'eighty', 90:'ninety', 100:'hundred', 1000:'thousand'
}
def number_to_words(n):
    if n==0:
        return ""
    elif n<=20:
        return number_to_words(n)
    elif n<100:
        tens, below_ten=divmod(n,10)
        return num_to_word[tens*10] + (num_to_word[below_ten] if below_ten else "")
    elif n<1000:
        hundreds, below_hundred=divmod(n,100)
        if below_hundred:
            return num_to_word[hundreds]+num_to_word[100]+("and"+number_to_words(below_hundred) if below_hundred else "")
        else:
            return num_to_word[hundreds] + num_to_word[100]
    elif n==1000:
        return "one"+num_to_word[1000]
    
total_letters=0
for i in range(1,1001):
    words=number_to_words(i)
    total_letters+=len(words.replace(" ","").replace("-",""))
    print(total_letters)
    
