from django.contrib.admin import widgets
from django.utils.safestring import mark_safe
from django.forms import MultiValueField, CharField, MultiWidget, TextInput

class MultiFileInput(widgets.AdminFileWidget):
 
    def render(self, name, value, attrs=None):
        attrs['multiple'] = 'true'
        output = super(MultiFileInput, self).render(name, value, attrs=attrs)
        return mark_safe(output)

class PhoneWidget(MultiWidget):
	def __init__(self, code_length=3, num_length=7, attrs=None):
		widgets = [TextInput(attrs={'size': code_length, 'maxlength': code_length}),
				TextInput(attrs={'size': num_length, 'maxlength': num_length})]
		super(PhoneWidget, self).__init__(widgets, attrs)

	def decompress(self, value):
		if value:
			return [value.code, value.number]
		else:
			return ['', '']


	def format_output(self, rendered_widgets):
		return '+7' + '(' + rendered_widgets[0] + ') - ' + rendered_widgets[1]


class PhoneField(MultiValueField):
    def __init__(self, code_length, num_length, *args, **kwargs):
        list_fields = [CharField(),
                       CharField()]
        super(PhoneField, self).__init__(list_fields, widget=PhoneWidget(code_length, num_length), *args, **kwargs)

    def compress(self, values):
        return '+7' + values[0] + values[1]  