from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from vsite import LHKit
from .models import FinanceType
from .serializer import FinanceTypeSerializer

@api_view(['POST'])
def typelist(request, format=None):
    ftypes = FinanceType.objects.all().order_by('-CreateDate')
    itCount = len(ftypes)
    page = int ( request.POST.get('page',1 ) )
    rows = int ( request.POST.get('rows', 5  ) )
   
    standRt = LHKit.LHStand.LHResult()
    if (page-1)*rows > itCount :
        standRt ['data'] = []
    else :
        lastPageNumber = rows
        if  ((page * rows) >= itCount ) :
            lastPageNumber = itCount - ((page - 1) * rows)
        ser = FinanceTypeSerializer(instance=ftypes[(page-1)*rows: (page-1)*rows + lastPageNumber] , many=True)
        standRt['data'] = ser.data
    return Response(data=standRt, status=status.HTTP_200_OK)

@api_view(['POST'])
def typedelete(request, format=None):
    itID = int ( request.POST.get('id',0 ) )
    ftypes = FinanceType.objects.get(pk=itID).delete();
    
    standRt = LHKit.LHStand.LHResult()
    standRt["msg"] = "删除成功了!"
    return Response(data=standRt, status=status.HTTP_200_OK)

