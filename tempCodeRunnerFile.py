import customtkinter
from customtkinter import filedialog
import os
from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("AI EVALUATOR")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(
            image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "evaluate.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="NAVIGATION MENU", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="MANNUAL CHECKING",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="CONTATC US",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(
            row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        # home frame
        self.analyze_upload_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color="transparent")
        self.analyze_upload_frame.grid(row=1, column=0, pady=10, padx=10, sticky="new")
        self.file_upload_btn = customtkinter.CTkButton(self.analyze_upload_frame, text="Upload PDF", command=self.upload_file)
        self.file_location_label = customtkinter.CTkLabel(self.analyze_upload_frame, text="No File Selected", text_color="red")
        self.file_upload_btn.grid(row=1, column=0, padx=20, pady=10)
        self.file_location_label.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.analyze_upload_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
        self.home_frame_button = customtkinter.CTkButton(self.analyze_upload_frame, text="EVALUATE", image=self.image_icon_image, command=self.analyze_btn)
        self.home_frame_button.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_button_4 = customtkinter.CTkButton(self.analyze_upload_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
        self.home_frame_button_4.grid(row=5, column=0, padx=20, pady=10)

        # analyze frame
        self.analyze_file_frame = customtkinter.CTkFrame(self.home_frame, corner_radius=0, fg_color="transparent")
        self.analyze_doc_label1 = customtkinter.CTkLabel(self.analyze_file_frame)
        self.analyze_doc_label1.grid(row=0, column=0, pady=5, padx=5, sticky="nw")
        # self.dumytext=customtkinter.CTkButton(self.analyze_file_frame,text="Button",)
        
        # self.dumytext.grid(row=1, column=0, pady=5, padx=5, sticky="nw")
        self.analyze_upload_agn_btn = customtkinter.CTkButton(self.analyze_file_frame, text="Upload Again", command=lambda: self.analyze_frame_switch("upload"))
        self.analyze_upload_agn_btn.grid(row=10, column=0, pady=5, padx=5, sticky="nw")
        # self.back_button = customtkinter.CTkButton(self.analyze_file_frame, text="Back", command=self.back_event, width=200)
        # self.back_button.grid(row=10, column=0, padx=30, pady=(15, 15))

        # create second frame
        self.second_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        # create third frame
        self.third_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(
            fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(
            fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_2":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()



    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


    def analyze_frame_switch(self, name):
        if name == "analyze":
            self.analyze_file_frame.grid(
                row=1, column=0, pady=10, padx=10, sticky="new")
        else:
            self.analyze_file_frame.grid_forget()
        if name == "upload":
            self.analyze_upload_frame.grid(
                row=1, column=0, pady=10, padx=10, sticky="new")
        else:
            self.analyze_upload_frame.grid_forget()

    def analyze_btn(self):
        self.analyze_frame_switch("analyze")
        print(file_path)
        self.analyze_doc_label1.configure(
            text="Crime Charge Name :function of ML")
        # self.analyze_upload_agn_btn.grid(row=2, column=0, padx=20, pady=10)

    def upload_file(self):
        global file_path
        file_path = filedialog.askopenfilename(
            filetypes=[("PDF File", '.pdf')])
        if (file_path):
            self.file_location_label.configure(
                text="File Selected: "+file_path, text_color="blue")
            self.home_frame_button.grid(
                row=4, column=0, padx=20, pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
