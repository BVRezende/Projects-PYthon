'''Nao Esquecer de add : pip install pillow e 
pip install qrcode no terminal antes de compilar'''
from tkinter import messagebox, Tk, Label, Entry, Button
import qrcode
from PIL import Image

def gera_qrcode():
    url=texto_URl.get()

    if len(url)==0:
        messagebox.showinfo(
            title='Erro',
            message='Favor inserir um URL válida'
        )
    else:
        opcao_escolhida = messagebox.askokcancel(
            title=url,
            message= f'O endereço URL é:\n'
                     f'Endereço:{url}\n'
                     f'Pronto para salvar?'
        )
        if opcao_escolhida:
             qr=qrcode.QRCode(version=1,box_size=10, border=5)
             qr.add_data(url)
             qr.make(fit=True)
        
             img= qr.make_image(fill_color='black', back_color='white')
             img.save('QRCODE.png')

             img=Image.open('QRCODE.png')
             img.show()
janela=Tk()

janela.title('Gerador de QR Code')
janela.config(padx=10, pady=30)

titulo_URl= Label(text='URL')
titulo_URl.grid(row=2, column=0)

texto_URl=Entry(width=35)
texto_URl.grid(row=2,column=1)
texto_URl.focus()


botao_gerar= Button(text='Gerar QR Code', width=20, command=gera_qrcode)
botao_gerar.grid(row=3, column=1)

janela.mainloop()
