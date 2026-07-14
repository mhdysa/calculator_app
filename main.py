from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy.utils import platform

class CalculatorApp(App):
    def build(self):
        # تنظیم اندازه پنجره برای موبایل
        if platform in ['android', 'ios']:
            Window.size = (Window.width, Window.height)
        else:
            Window.size = (350, 550)
        
        # تنظیم رنگ پس‌زمینه
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        
        return CalculatorLayout()

class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(CalculatorLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 8
        self.padding = [15, 20, 15, 20]
        
        # نمایشگر با طراحی زیبا
        self.display = TextInput(
            text='0',
            font_size=50,
            readonly=True,
            halign='right',
            multiline=False,
            size_hint=(1, 0.25),
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1),
            cursor_color=(0, 0, 0, 0),
            padding=[20, 20, 20, 20]
        )
        self.add_widget(self.display)
        
        # دکمه‌های ردیف اول (عملیات ویژه)
        special_buttons = [
            ['C', '±', '%', '÷']
        ]
        self.add_button_row(special_buttons, is_special=True)
        
        # دکمه‌های اصلی
        buttons = [
            ['7', '8', '9', '×'],
            ['4', '5', '6', '−'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '⌫']
        ]
        
        for row in buttons:
            self.add_button_row([row], is_special=False)
        
        # متغیرهای برنامه
        self.current_input = '0'
        self.expression = ''
        self.result_shown = False
        self.last_operator = ''
        self.last_number = ''

    def add_button_row(self, buttons_list, is_special=False):
        """اضافه کردن ردیف دکمه‌ها"""
        for row in buttons_list:
            h_layout = BoxLayout(spacing=8, size_hint=(1, 0.15))
            
            for label in row:
                if label in ['C', '±', '%', '÷', '×', '−', '+', '=']:
                    # دکمه‌های عملیاتی
                    if label == '=':
                        btn = Button(
                            text=label,
                            font_size=35,
                            background_normal='',
                            background_color=(0.2, 0.6, 0.9, 1),
                            color=(1, 1, 1, 1),
                            bold=True
                        )
                    elif label in ['C']:
                        btn = Button(
                            text=label,
                            font_size=30,
                            background_normal='',
                            background_color=(0.9, 0.3, 0.3, 1),
                            color=(1, 1, 1, 1),
                            bold=True
                        )
                    else:
                        btn = Button(
                            text=label,
                            font_size=30,
                            background_normal='',
                            background_color=(0.3, 0.3, 0.3, 1),
                            color=(1, 1, 1, 1),
                            bold=True
                        )
                else:
                    # دکمه‌های عددی
                    btn = Button(
                        text=label,
                        font_size=30,
                        background_normal='',
                        background_color=(1, 1, 1, 1),
                        color=(0, 0, 0, 1),
                        bold=True
                    )
                    # اضافه کردن سایه به دکمه‌های عددی
                    btn.color = (0.1, 0.1, 0.1, 1)
                
                btn.bind(on_press=self.on_button_press)
                h_layout.add_widget(btn)
            
            self.add_widget(h_layout)

    def on_button_press(self, instance):
        """مدیریت کلیک روی دکمه‌ها"""
        button_text = instance.text
        
        # پردازش دکمه‌ها
        if button_text == 'C':
            self.clear_all()
        elif button_text == '⌫':
            self.backspace()
        elif button_text == '±':
            self.toggle_sign()
        elif button_text == '%':
            self.percentage()
        elif button_text == '=':
            self.calculate()
        elif button_text in ['÷', '×', '−', '+']:
            self.add_operator(button_text)
        else:
            self.add_number(button_text)

    def clear_all(self):
        """پاک کردن همه چیز"""
        self.current_input = '0'
        self.expression = ''
        self.result_shown = False
        self.last_operator = ''
        self.last_number = ''
        self.update_display()

    def backspace(self):
        """حذف آخرین کاراکتر"""
        if self.result_shown:
            self.clear_all()
            return
        
        if len(self.current_input) > 1:
            self.current_input = self.current_input[:-1]
        else:
            self.current_input = '0'
        self.update_display()

    def toggle_sign(self):
        """تغییر علامت عدد"""
        if self.current_input and self.current_input != '0':
            if self.current_input.startswith('-'):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = '-' + self.current_input
            self.update_display()

    def percentage(self):
        """محاسبه درصد"""
        try:
            num = float(self.current_input)
            self.current_input = str(num / 100)
            self.update_display()
        except ValueError:
            pass

    def add_number(self, number):
        """اضافه کردن عدد به نمایشگر"""
        if self.result_shown:
            self.clear_all()
            self.result_shown = False
        
        if number == '.':
            if '.' not in self.current_input:
                self.current_input += '.'
        else:
            if self.current_input == '0' and number != '.':
                self.current_input = number
            else:
                # محدودیت طول عدد
                if len(self.current_input) < 15:
                    self.current_input += number
        self.update_display()

    def add_operator(self, operator):
        """اضافه کردن عملگر"""
        # تبدیل عملگرهای نمایشی به عملگرهای واقعی
        operator_map = {
            '÷': '/',
            '×': '*',
            '−': '-',
            '+': '+'
        }
        real_operator = operator_map.get(operator, operator)
        
        if self.current_input:
            # اگر عملگر قبلی وجود داشت، محاسبه انجام شود
            if self.expression and self.last_operator:
                self.calculate()
            
            self.expression = self.current_input + real_operator
            self.last_operator = real_operator
            self.current_input = '0'
            self.result_shown = False
            self.update_display()

    def calculate(self):
        """محاسبه نتیجه نهایی"""
        if self.expression and self.current_input:
            try:
                # ساخت عبارت ریاضی
                full_expression = self.expression + self.current_input
                
                # جایگزینی عملگرها برای eval
                full_expression = full_expression.replace('×', '*')
                full_expression = full_expression.replace('÷', '/')
                full_expression = full_expression.replace('−', '-')
                
                # محاسبه با دقت بالا
                result = eval(full_expression)
                
                # گرد کردن نتیجه
                if isinstance(result, float):
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result, 10)
                
                self.current_input = str(result)
                self.expression = ''
                self.last_operator = ''
                self.result_shown = True
                self.update_display()
                
            except ZeroDivisionError:
                self.current_input = 'خطا: تقسیم بر صفر'
                self.expression = ''
                self.last_operator = ''
                self.update_display()
            except Exception as e:
                self.current_input = 'خطا'
                self.expression = ''
                self.last_operator = ''
                self.update_display()

    def update_display(self):
        """به‌روزرسانی نمایشگر"""
        self.display.text = self.current_input

if __name__ == '__main__':
    CalculatorApp().title = 'ماشین حساب'
    CalculatorApp().icon = 'a.ico'  # تنظیم آیکون
    CalculatorApp().run()
