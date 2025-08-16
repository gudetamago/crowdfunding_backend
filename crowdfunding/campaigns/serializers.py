from rest_framework import serializers
from django.apps import apps
 
class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('campaigns.Campaign')
        fields = '__all__'

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('campaigns.Pledge')
        fields = '__all__'

class CampaignDetailSerializer(CampaignSerializer):
    pledges = PledgeSerializer(many=True, read_only=True) 
    # read_only because you don't wnat to be updating data