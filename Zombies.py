def Compute_gcd(a, b):
    if b == 0:
        return a
    else:
        return Compute_gcd(b, a%b)

perfect = []

percentage = input()
percentage = percentage.split(',')
percentage = [int(x) for x in percentage]
print(percentage)

cities = int(input('Enter no. of cities'))

for i in range(0, cities):
    try:
        if percentage[i] >  percentage[i + 1]:
            gdc = Compute_gcd(percentage[i], percentage[i + 1])
            if gdc == 1:
                perfect.append(i)
            else:
                pass
        else:
            pass
    except IndexError as e:
        # print(e)
        break
print(perfect[0])

