from rest_framework import serializers
from django.apps import apps
 
class CampaignSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.id') # "source" because it comes from another model

    class Meta:
        model = apps.get_model('campaigns.Campaign')
        fields = '__all__'
        # exclude owner   <- don't do this, this will exclude owner but it won't return the data either to the front end

class PledgeSerializer(serializers.ModelSerializer):

    supporter = serializers.ReadOnlyField(source='supporter.id')

    class Meta:
        model = apps.get_model('campaigns.Pledge')
        fields = '__all__'

class CampaignDetailSerializer(CampaignSerializer):
    pledges = PledgeSerializer(many=True, read_only=True) 
    # read_only because you don't want to be updating data

class StretchSerializer(serializers.ModelSerializer):

    campaign = serializers.ReadOnlyField(source='campaign.id')

    class Meta:
        model = apps.get_model('campaigns.Stretch')
        fields = '__all__'
