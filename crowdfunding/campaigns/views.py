from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Campaign
from .serializers import CampaignSerializer

class CampaignList(APIView):

    def get(self, request):
       
       campaigns = Campaign.objects.all()
       serializer = CampaignSerializer(campaigns, many=True)
       return Response(serializer.data)
    
    def post(self, request):
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class CampaignDetail(APIView):

    def get_object(self, pk):
        try:
            campaign = Campaign.objects.get(pk=pk)
            return campaign
        except Campaign.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        campaign = self.get_object(pk)
        serializer = CampaignSerializer(campaign)
        return Response(serializer.data)
