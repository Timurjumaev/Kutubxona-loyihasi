from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from .forms import *

def loginView(request):
    if request.method=='POST':
        user=authenticate(
            username=request.POST.get('l'),
            password=request.POST.get('p')
        )
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/bosh/')
    return render(request, 'asosiy.html')

def logoutView(request):
    logout(request)
    return redirect('/')

def bosh(request):
    if request.user.is_authenticated:
        return render(request, 'bosh.html')
    else:
        return redirect('/')
def husan(request):
    if request.user.is_authenticated:

        return render(request, 'husan.html')
    else:
        return redirect('/')




def student(request):
    if request.method=='POST':
        f=StudentForm(request.POST)
        if f.is_valid():
            Student.objects.create(
                ism=f.cleaned_data.get('i'),
                jins=f.cleaned_data.get('j'),
                kitob_soni=f.cleaned_data.get('kitoblari_soni'),
                bitiruvchi=f.cleaned_data.get('bitiruvchi')
            )
        return redirect('/student/')
    soz = request.GET.get('q_sozi')
    if soz is None:
        s=Student.objects.all()
    else:
        s=Student.objects.filter(ism__contains=soz)
    data={
        'student': s,
        'forma': StudentForm
    }
    return render(request, 'students.html', data)

def bitiruvchi(request):

    data={
        'student': Student.objects.filter(bitiruvchi=True)
    }
    return render(request, 'mashq/bitiruvchi.html', data)

def kitob(request):
    data={
        'student': Student.objects.filter(kitob_soni__gt=0)
    }
    return render(request, 'mashq/kitob.html', data)

def talaba(request, son):
    data={
        'student' : Student.objects.get(id=son)
    }
    return render(request, 'mashq/tanlangan.html', data)





def talaba_ochir(request, son):
    t1=Student.objects.get(id=son)
    t1.delete()
    return redirect('/student/')

def books(request):
    if request.method=="POST":
        forma=KitobForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect('/books/')
    data={
        'books': Kitob.objects.all(),
        'forma': KitobForm
    }
    return render(request, 'mashq/books.html', data)

def kitob1(request, son):
    data={
        'kitob': Kitob.objects.get(id=son)
    }
    return render(request, 'mashq/kitob.html', data)

def student_tahrirlash(request, son):
    if request.method=="POST":
        if request.POST.get('bitiradi') is None:
            n=False
        else:
            n=True
        Student.objects.filter(id=son).update(
            ism=request.POST.get('ismi'),
            bitiruvchi=n,
            kitob_soni=request.POST.get('k_soni')
        )
        return redirect('/student/')
    data={
        'student':Student.objects.get(id=son)
    }
    return render(request, 'student-edit.html', data)

def talaba_tasdiqlash(request, son):
    data={
        'talaba':Student.objects.get(id=son)
    }
    return render(request, 'talaba_ochir.html', data)

def mualliflar(request):
    if request.method=='POST':
        if request.POST.get('tirik')=='on':
            t=True
        else:
            t=False
        Muallif.objects.create(
            ism=request.POST.get('ism'),
            tirik=t,
            kitob_soni=request.POST.get('kitob_soni'),
            tugilgan_yil=request.POST.get('tugilgan_yil')
        )
        return redirect('/mualliflar/')

    soz=request.GET.get('q_sozi')
    if soz is None:
        s=Muallif.objects.all()
    else:
        s=Muallif.objects.filter(ism__contains=soz)
    data={
        'mualliflar': s
    }
    return render(request, 'mualliflar.html', data)

def muallif_delete(request, son):
    data={
        'muallif': Muallif.objects.get(id=son)
    }
    return render(request, 'tasdiq_m.html', data)
def delete_m(request, son):
    Muallif.objects.get(id=son).delete()
    return redirect('/mualliflar/')

def muallif(request, son):
    data={
        'muallif': Muallif.objects.get(id=son)
    }
    return render(request, 'muallif.html', data)

def muallif_t(request, son):
    if request.method=="POST":
        if request.POST.get('t')=="on":
            s=True
        else:
            s=False
        Muallif.objects.filter(id=son).update(
            ism=request.POST.get('i'),
            tirik=s,
            kitob_soni=request.POST.get('k'),
            tugilgan_yil=request.POST.get('ty'),
        )
        return redirect('/mualliflar/')
    data = {
        'muallif': Muallif.objects.get(id=son)
    }
    return render(request, 'muallif_t.html', data)

def recordlar(request):
    if request.method=='POST':
        q=request.POST.get('q')
        if q=='on':
            q=True
        else:
            q=False
        Record.objects.create(
            student=Student.objects.get(ism=request.POST.get('student')),
            kitob=Kitob.objects.get(nom=request.POST.get('kitob')),
            olingan_sana=request.POST.get('os'),
            qaytardi=q,
            qaytargan_sana=request.POST.get('qs')
        )
        return redirect('/recordlar/')
    soz = request.GET.get('q_sozi')
    if soz is None:
        s = Record.objects.all()
    else:
        s = Record.objects.filter(student__ism__contains=soz)
    data={
        "recordlar": s,
        'studentlar': Student.objects.all(),
        'kitoblar': Kitob.objects.all()

    }
    return render(request, 'recordlar.html', data)

def rdelete(request, son):
    data={
        'record': Record.objects.get(id=son)
    }
    return render(request, 'tasdiq_r.html', data)

def delete_r(request, son):
    Record.objects.get(id=son).delete()
    return redirect('/recordlar/')

def tirik(request):
    data={
        'tirik': Muallif.objects.filter(tirik=True)
    }
    return render(request, 'tirik.html', data)

def katta_kitob(request):
    data={
        'katta': Kitob.objects.order_by('-sahifa')[:3]
    }
    return render(request, 'katta.html', data)

def kitobi_kop(request):
    data={
        'kop': Muallif.objects.order_by('-kitob_soni')[:3]
    }
    return render(request, 'kop.html', data)

def last_record(request):
    data={
        'last_record': Record.objects.order_by('-olingan_sana')[:3]
    }
    return render(request, 'last_record.html', data)

def mk(request):
    data={
        'mk': Kitob.objects.filter(muallif__tirik=True)
    }
    return render(request, 'mk.html', data)
def badiiy(request):
    data={
        'badiiy': Kitob.objects.filter(janr='Badiiy')
    }
    return render(request, 'badiiy.html', data)

def isma(request):
    data={
        'isma': Student.objects.filter(ism__contains='a')
    }
    return render(request, 'isma.html', data)

def tyil(request):
    data={
        'tyil': Muallif.objects.order_by('tugilgan_yil')[:3]
    }
    return render(request, 'tyil.html', data)

def km(request):
    data={
        'km': Kitob.objects.filter(muallif__kitob_soni__lt=10)
    }
    return render(request, 'km.html', data)

def erkak(request):
    data={
        'erkak': Student.objects.filter(jins='erkak')
    }
    return render(request, 'erkak.html', data)

def rid(request, son):
    data={
        'rid': Record.objects.get(id=son)
    }
    return render(request, 'rid.html', data)

def bitir(request):
    data={
        'bitir': Record.objects.filter(student__bitiruvchi=True)
    }
    return render(request, 'bitir.html', data)

def record_t(request, son):
    if request.method=='POST':
        if request.POST.get('q')=='on':
            s=True
        else:
            s=False
        Record.objects.filter(id=son).update(
            qaytardi=s,
            qaytargan_sana=request.POST.get('qs'),
        )
        return redirect('/recordlar/')
    data={
        'record': Record.objects.get(id=son)
    }
    return render(request, 'record_t.html', data)

def delete_k(request, son):
    Kitob.objects.get(id=son).delete()
    return redirect('/books/')
def book_delete(request, son):
    data={
        'kitob': Kitob.objects.get(id=son)
    }
    return render(request, 'tasdiq_k.html', data)

def register(request):
    if request.method=='POST':
        User.objects.create(
            username=request.POST.get('l'),
            password=request.POST.get('p')
        )
        return redirect('/bosh/')
    return render(request, 'register.html')