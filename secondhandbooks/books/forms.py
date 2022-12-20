class BookForm(forms.ModelForm):
    """
    Class user validated book and created new 
    """

    class Meta:
        model = Book
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """
    Class user validated review in the book and created new  
    """
    CHOICES = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))
    review = forms.ChoiceField(choices=CHOICES, label="Rate", widget=forms.Select)

    class Meta:
        model = Review
        fields = ('review', )
