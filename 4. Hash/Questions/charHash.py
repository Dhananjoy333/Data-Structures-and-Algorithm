# def charDup(str):
#     hashList = [0]*26
#     hashMap= {}
#     for i in str:
#         value = ord(i) - 97
#         hashList[value] += 1
#     for i in str:
#         hashMap[i] = hashList[ord(i)-97]
#     print(hashMap)
# charDup("dhananjoy")

# best beacuse it hanfles symbols also
# def charDup(str):
#     hashMap = {}
#     for ch in str:
#         hashMap[ch] = hashMap.get(ch,0) + 1
#     print(hashMap)
# charDup("Ddhanan@_--joy")


