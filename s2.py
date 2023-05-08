# string = "you and me and sara are friend and"
# # print(string.split().count('and'))
# print(string.count("and"))

# # exercise :    با کمک حلقه  تعداد تکرار کلمه
# # and
# # را نمایش دهید
# all_words = []
# word = ''
# counter = 0
# and_counter = 0
# for s in string:
#     word += s
#     counter += 1
#     if s == ' ':
#         all_words.append(word[:-1])
#         if word[:-1] == 'and':
#             and_counter += 1
#         word = ''
#     # if counter == len(string):
#     #     all_words.append(word)
# else:
#     all_words.append(word)
#     if word == 'and':
#         and_counter += 1


# print(and_counter)
# print(all_words)

MONTHS = "JanFebMarAprMayJunJulAugSepOctNovDec"
month_number = int(input('enter month`s number: '))


# exercise 1:
# سه رنگ قرمز، سبز و آبی داریم
# می خواهیم یک ستاره با کمک ترتل بکشیم
# هر یک از خط های ستاره باید یکی از رنگ های بالا را داشته باشد.
# هربار که برنامه اجرا می شود، می بایست یک رنگ به عنوان رنگ پر کردن ستاره انتخاب شود
# این رنگ به صورت تصادفی می بایست انتخاب گردد
#exercise2 : rotated squares  هر یک از مربع ها یکی از رنگ های سبز، ابی و یا قرمز را داشته باشند