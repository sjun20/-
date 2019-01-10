from django.shortcuts import render , get_object_or_404 , redirect
from django.utils import timezone
import datetime
from .models import Parking , Reserve
from .forms import ParkingForm , ReserveForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def parking_list(request):
    parkings = Parking.objects.all()
    context = {'parkings':parkings}

    return render(request, 'blog/parking_list.html', context)
#@login_required 이거 추가하면 로그인 해야 보임
def parking_detail(request, pk):
    parking = get_object_or_404(Parking, pk=pk)
    today = datetime.date.today()
    appoint = Reserve.objects.filter(parking=pk, start__date=today)



    context = {"parking":parking,"today":today,"appoint":appoint}
    return render(request, 'blog/parking_detail.html', context)

def parking_new(request):
    if request.method == "POST":
        form = ParkingForm(request.POST)
        if form.is_valid():
            parking = form.save(commit=False)
            parking.author = request.user
            parking.published_date = timezone.now()
            parking.save()
            return redirect('parking_detail', pk=parking.pk)
    else:
        form = ParkingForm()
    return render(request, 'blog/parking_edit.html', {'form': form})

def parking_edit(request, pk):
    parking = get_object_or_404(Parking, pk=pk)
    if request.method == "POST":
        form = ParkingForm(instance=parking)
        if form.is_valid():
            parking = form.save(commit=False)
            parking.author = request.user
            parking.published_date = timezone.now()
            parking.save()
            return redirect('parking_detail', pk=parking.pk)
    else:
        form = ParkingForm(instance=parking)
    return render(request, 'blog/parking_edit.html', {'form': form})

def add_reserve_to_parking(request, pk):
    parking = get_object_or_404(Parking, pk=pk)
    if request.method == "POST":
        form = ReserveForm(request.POST)
        if form.is_valid():
            reserve = form.save(commit=False)
            reserve.parking = parking
            reserve.save()
            return redirect('parking_detail', pk=parking.pk)
    else:
        form = ReserveForm()
    return render(request, 'blog/add_reserve_to_parking.html', {'form': form})

def reserve_detail(request, pk, pk2):

    parking = get_object_or_404(Parking, pk=pk)


    reserve = Reserve.objects.get(parking=pk, pk=pk2)
    now = datetime.datetime.now()

    start_charge = reserve.start.strftime("%Y-%m-%d %H:%M:%S")
    end_charge = reserve.end.strftime("%Y-%m-%d %H:%M:%S")

    start_year = start_charge[0:4]
    start_month = start_charge[5:7]
    start_day = start_charge[8:10]
    start_hour = start_charge[11:13]
    start_minute = start_charge[14:16]

    end_year = end_charge[0:4]
    end_month = end_charge[5:7]
    end_day = end_charge[8:10]
    end_hour = end_charge[11:13]
    end_minute = end_charge[14:16]
    aaa = 39494

    time = reserve.end - reserve.start
    #시간당 요금계산 구현해야함

    bill = 1000



    context = {"parking":parking,"reserve":reserve,"bill":bill,"start_charge":start_charge,"end_charge":end_charge,"time":time}

    return render(request, 'blog/reserve_detail.html', context)

def reserve_remove(request, pk, pk2):
    parking = get_object_or_404(Parking, pk=pk)
    reserve = Reserve.objects.get(parking=pk, pk=pk2)
    reserve.delete()
    return redirect('parking_list')
