from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
import joblib

class formTextInput(TextInput):

    def __init__(self, **kwargs):
        super(formTextInput,self).__init__(**kwargs)

        self.multiline = False
        self.font_size = 18
        self.size_hint = (1,1.5)
        self.size = (1000,300)        

class formTextLabel(Label):

    def __init__(self,**kwargs):
        super(formTextLabel,self).__init__(**kwargs)

        self.font_size = 20



class EnvattoRealEstates(App):

    def build(self):

        self.icon = 'favicon.png'
        self.title = 'Envatto Real Estates'

        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.8,0.8)
        self.window.pos_hint = {'center_x':.5,'center_y':.5}
        self.window.padding = (10,10)

        self.header = GridLayout()
        self.header.cols = 1
        self.header.padding = (20,20)

        self.appName = Label(

                            text = 'House Price Prediction',
                            font_family = 'Sofia',
                            font_size = 30,
                            outline_color = 'blue',
                            outline_width = 3,

                        )


        self.header.add_widget(self.appName)
        self.window.add_widget(self.header)

        # Area

        self.form_item_cont_1 = BoxLayout(orientation = 'vertical')
        self.form_item_cont_1.padding = (10,10)

        self.area_label =  formTextLabel(
                                    text = 'Area'
                                   )
        self.area_input = formTextInput(

                            input_type = 'number'

                        )
    
       

        self.form_item_cont_1.add_widget(self.area_label)
        self.form_item_cont_1.add_widget(self.area_input)

        self.window.add_widget(self.form_item_cont_1)

        #Bedrooms
        self.form_item_cont_2 = BoxLayout(orientation = 'vertical')
        self.form_item_cont_2.padding = (10,10)

        self.bedrom_label = formTextLabel(
                            text = 'Bedrooms',
                        )

        self.bedroom_input = formTextInput(
                            input_type = 'number'                            
                        )
    
       
        self.form_item_cont_2.add_widget(self.bedrom_label)
        self.form_item_cont_2.add_widget(self.bedroom_input)

        self.window.add_widget(self.form_item_cont_2)

        #Bathrooms

        self.form_item_cont_3 = BoxLayout(orientation = 'vertical')
        self.form_item_cont_3.padding = (10,10)

        self.bathroom_label = formTextLabel(
                            text = 'Bathrooms',
                        )

        self.bathroom_input = formTextInput(
                            input_type = 'number'

                        )
    
       
        self.form_item_cont_3.add_widget(self.bathroom_label)
        self.form_item_cont_3.add_widget(self.bathroom_input)
        
        self.window.add_widget(self.form_item_cont_3)

        self.btn_cont = GridLayout()
        self.btn_cont.cols = 1
        self.btn_cont.pos_hint = {'center_x':0.5,'center_y':0.5}
        self.btn_cont.size_hint = (0.5,0.6)

        self.submit_btn = Button(

                            text = 'Submit',
                            background_color = 'blue',
                            size_hint = (0.3,0.6),
                            pos_hint = {'center_x':0.5,'center_y':0.5}

                            )

        self.submit_btn.bind(on_press = self.predict)

        self.btn_cont.add_widget(self.submit_btn)
    
        self.window.add_widget(self.btn_cont)
        self.error_label = Label(

                        text = '',
                        size_hint = (0,0)
                    )
                
        self.res_label = Label(

                        text = 'HIET',
                        size_hint = (1,1)                      
                    )

        self.window.add_widget(self.res_label)
        self.window.add_widget(self.error_label)
        
        return self.window

    def predict(self,instance):
        area = self.area_input.text
        n_bed = self.bedroom_input.text
        n_bath = self.bathroom_input.text

        try: 
            int(area)
            int(n_bed)
            int(n_bath)
        except:
            area = 0
            n_bed = 0
            n_bath = 0
        

        if area == 0: 
            val = ""

        else:

            model = joblib.load('housingModel2.sav')
            
            pred =  model.predict([[int(area),int(n_bed),int(n_bath)]])
            val = f'House Price: {int(pred[0])}USD\n'
                            
            self.res_label.font_size = 20
            self.res_label.text = val
            
 
                
            

                    


if __name__ == '__main__':
    EnvattoRealEstates().run()

