# class WhatsApp:
#     def chat(self):
#         print('this is chat feature')



# class WhatsApp_Emoji_update(WhatsApp):
#     def emoji(self):
#         print('this is emoji feature')


# class WhatsApp_sticker_update(WhatsApp_Emoji_update):
#     def sticker(self):
#         print('this is sticker feature')




# # x=WhatsApp()
# # x.chat()y

# y=WhatsApp_sticker_update()
# y.chat()
# y.emoji()
# y.sticker()




class A:
    def colour(self):
        print("red")

class B:
    def shape(self):
        print("round")


class C(A,B):
    def pro(self):
        print('final product')




a=C()

a.colour()
a.shape()
a.pro()