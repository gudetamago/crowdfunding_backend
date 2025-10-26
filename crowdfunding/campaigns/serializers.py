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
    nickname = serializers.ReadOnlyField(source='supporter.nickname')
    alt_nickname = serializers.ReadOnlyField(source='supporter.alt_nickname')

    class Meta:
        model = apps.get_model('campaigns.Pledge')
        fields = '__all__'

class CampaignDetailSerializer(CampaignSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    # read_only because you don't want to be updating data
    amount_pledged = serializers.IntegerField(default=0)
    total_unique_supporters = serializers.IntegerField(default=0)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title) # If there's no 'title' to update, just put the old value back
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = instance.date_created
        instance.owner = validated_data.get('owner', instance.owner)
        instance.alt_title = validated_data.get('alt_title', instance.alt_title) # If there's no 'title' to update, just put the old valiue back
        instance.alt_description = validated_data.get('alt_description', instance.alt_description)
        instance.alt_image = validated_data.get('alt_image', instance.alt_image)
        instance.save()
        return instance

class PledgeDetailSerializer(PledgeSerializer):
    
    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.campaign = instance.campaign
        instance.supporter = instance.supporter
        instance.save()
        return instance


class StretchSerializer(serializers.ModelSerializer):

    campaign = serializers.ReadOnlyField(source='campaign.id')

    class Meta:
        model = apps.get_model('campaigns.Stretch')
        fields = '__all__'
