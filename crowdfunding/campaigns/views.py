from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Campaign, Pledge, Stretch
from .serializers import CampaignSerializer, CampaignDetailSerializer, PledgeSerializer, StretchSerializer

class CampaignList(APIView):

    def get(self, request):
       
       campaigns = Campaign.objects.all()
       serializer = CampaignSerializer(campaigns, many=True)
       return Response(serializer.data)
    
    def post(self, request):
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user) # This will assign owner to be the currently logged in user
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
        serializer = CampaignDetailSerializer(campaign)
        return Response(serializer.data)

class PledgeList(APIView):

    def get(self, request):
       
       pledges = Pledge.objects.all()
       serializer = PledgeSerializer(pledges, many=True)
       return Response(serializer.data)
    
    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class StretchList(APIView):

    def get(self, request, pk):
        stretches = Stretch.objects.filter(campaign_id=pk)
        serializer = StretchSerializer(stretches, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = StretchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(campaign_id=pk)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


