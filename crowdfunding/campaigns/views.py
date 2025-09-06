from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from django.db.models import Sum
from .models import Campaign, Pledge, Stretch
from .serializers import CampaignSerializer, CampaignDetailSerializer, PledgeSerializer, PledgeDetailSerializer, StretchSerializer
from .permissions import IsOwnerOrReadOnly, isSupporterOrReadOnly

class CampaignList(APIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            campaign = Campaign.objects.get(pk=pk)
            self.check_object_permissions(self.request,  campaign)
            return campaign
        except Campaign.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        campaign = self.get_object(pk)
        amount_pledged = campaign.pledges.aggregate(total=Sum('amount'))['total'] or 0
        campaign.amount_pledged = amount_pledged  # Set the amount_pledged attribute
        
        serializer = CampaignDetailSerializer(campaign)

        return Response(serializer.data)
    
    def put(self, request, pk):
        campaign = self.get_object(pk)
        serializer = CampaignDetailSerializer(
            instance=campaign,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

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

class PledgeDetail(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        isSupporterOrReadOnly
    ]

    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request,  pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(pledge)
        return Response(serializer.data)
    
    def put(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(
            instance=pledge,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
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


