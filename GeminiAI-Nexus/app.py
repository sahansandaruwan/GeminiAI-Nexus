import customtkinter as ctk
import google.generativeai as genai
from deep_translator import GoogleTranslator

root = ctk.CTk()


def PasteText():
    CopiedText = root.clipboard_get()
    ApiEntry.insert(ctk.END, CopiedText)
    #print(ApiEntry.get())


#Exitapplication @SAHANSANDARUWAN   
def ExitUI():
    root.destroy()


#GeminiAI @SAHANSANDARUWAN
def engine():
    genai.configure(api_key=ApiEntry.get())

    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              )

    
    response = model.generate_content(InputLable.get())
    try:
        if response.prompt_feedback.block_reason == 0:
             PromtResult.delete("1.0", ctk.END)
             PromtResult.insert("0.0",response.text)
             
        else:
            PromtResult.delete("1.0", ctk.END)
            PromtResult.insert("0.0" ,'This content may violate our content policy :(')
        
    except:
        PromtResult.delete("1.0", ctk.END)
        PromtResult.insert("0.0" ,'Contact Developer ')



ctk.set_appearance_mode("dark")
root.geometry('750x670')
root.title('GeminiAI Nexus')

TitleLable = ctk.CTkLabel(root , text='GeminiAI Nexus\n @Sahan Sandaruwan', font=ctk.CTkFont(size=13))
TitleLable.pack(padx = 10,pady = (20,40))

frame = ctk.CTkFrame(root)
frame.pack(fill = 'x',padx = 100)


#APIFRAME @SAHANSANDARUWAN
ApiFrame = ctk.CTkFrame(frame)
ApiFrame.pack(padx = 100,pady=(20,5),fill = 'both')

ApiLable = ctk.CTkLabel(ApiFrame , text='Enter a API here')
ApiLable.pack()

ApiEntry =  ctk.CTkEntry(ApiFrame, placeholder_text="" , width=300)
ApiEntry.pack(pady = 10)



PasteButton = ctk.CTkButton(ApiFrame, text="Paste", command=PasteText)
PasteButton.pack(pady=10)


#OUTPUTLANGUAGEFRAME @SAHANSANDARUWAN
LanguageFrame = ctk.CTkFrame(frame)
LanguageFrame.pack(padx = 100,pady=(20,5),fill = 'both')

LanguageLable = ctk.CTkLabel(LanguageFrame , text='Select Output Language')
LanguageLable.pack()

LanguageDropdown = ctk.CTkComboBox(LanguageFrame ,values = ['en', 'si', 'es','fr', 'de', 'ru', 'ar', 'ja', 'hi', 'bn', 'pt', 'ur', 'ko', 'tr', 'it'])
LanguageDropdown.pack(pady =10)


#GeminiAI @SAHANSANDARUWAN
def engine():
    genai.configure(api_key=ApiEntry.get())

    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              )

    
    response = model.generate_content(InputLable.get())
    try:
        if response.prompt_feedback.block_reason == 0:
             PromtResult.delete("1.0", ctk.END)
             #PromtResult.insert("0.0",response.text)
             translated_text = GoogleTranslator(source='auto', target=LanguageDropdown.get()).translate(response.text)
             PromtResult.insert("0.0",translated_text)
             
        else:
            PromtResult.delete("1.0", ctk.END)
            PromtResult.insert("0.0" ,'This content may violate our content policy :(')
        
    except:
        PromtResult.delete("1.0", ctk.END)
        PromtResult.insert("0.0" ,'Error! Contact Developer :(')



#USERPROMT @SAHANSANDARUWAN
InputFrame = ctk.CTkFrame(frame)
InputFrame.pack(padx = 100,pady=(20,5),fill = 'both')

InputLable = ctk.CTkLabel(InputFrame , text='Enter a promt here')
InputLable.pack()

InputLable =  ctk.CTkEntry(InputFrame, placeholder_text="" , width=300)
InputLable.pack(pady = 10)


GenarateButton = ctk.CTkButton(frame, text="Send Promt", command=engine)
GenarateButton.pack(pady=10)

PromtResult = ctk.CTkTextbox(root , font=ctk.CTkFont(size=12))
PromtResult.pack(pady = 10 , fill = "x" , padx = 20)


root.mainloop()
