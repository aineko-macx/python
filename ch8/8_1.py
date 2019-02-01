def reverse(s):
    
    if len(s) == 0:
        return
    print(s[-1])
    reverse(s[0:-1])


reverse("Chargers")
