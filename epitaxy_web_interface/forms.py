from django import forms

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Column, Row, Submit

from .models import Experiment


class ExperimentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Row(
                Column('code', css_class='form-group col col-md-2'),
                Column('group', css_class='form-group col col-md-2'),
                Column('labels', css_class='form-group col col-md-4'),
                css_class='row'
            ),
            Row(
                Column('recipe_layer_number_tdms', css_class='form-group col col-md-4'),
                css_class='row'
            ),
            Row(
                Column('recipe_log', css_class='form-group col col-md-4'),
                Column('shutter_csv', css_class='form-group col col-md-4'),
                css_class='row'
            ),
            
            Row(
                Column('curvature_tdms', css_class='form-group col col-md-4'),
                Column('roughness_tdms', css_class='form-group col col-md-4'),
                css_class='row'
            ),
            Row(
                Column('wafer_temperature_tdms', css_class='form-group col col-md-4'),
                Column('reflectivity_tdms', css_class='form-group col col-md-4'),
                css_class='row'
            ),

            Submit(
                'submit', 'Valider',
                css_class='btn btn-secondary my-5'
            )
        )

    class Meta:
        model = Experiment
        fields = '__all__'
