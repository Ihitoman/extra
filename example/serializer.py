from rest_framework import routers, serializers



from example.models import Actividad
from example.models import Cosa


class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ('__all__')

class CosaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cosa
        fields = ('__all__')



