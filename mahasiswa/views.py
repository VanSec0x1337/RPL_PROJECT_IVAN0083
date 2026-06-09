from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Mahasiswa


@login_required(login_url='/accounts/login/')
def index(request):
    context = {
        'judul': 'Halo Mahasiswa',
        'deskripsi': 'Contoh halaman index menggunakan Django templates dan static files.'
    }
    return render(request, 'mahasiswa/index.html', context)


@login_required(login_url='/accounts/login/')
def daftar_mahasiswa(request):
    mahasiswa = Mahasiswa.objects.all()
    return render(request, 'mahasiswa/daftar.html', {'mahasiswa': mahasiswa})


@login_required(login_url='/accounts/login/')
def tambah_mahasiswa(request):
    error = ''
    nim = ''
    nama = ''
    programstudi = ''

    if request.method == 'POST':
        nim = request.POST.get('nim', '').strip()
        nama = request.POST.get('nama', '').strip()
        programstudi = request.POST.get('programstudi', '').strip()

        if not nim or not nama or not programstudi:
            error = 'Harap isi semua field terlebih dahulu.'
            messages.error(request, error)
        else:
            Mahasiswa.objects.create(nim=nim, nama=nama, programstudi=programstudi)
            return redirect('daftar_mahasiswa')

    return render(request, 'mahasiswa/tambah.html', {
        'error': error,
        'nim': nim,
        'nama': nama,
        'programstudi': programstudi,
    })


@login_required(login_url='/accounts/login/')
def edit_mahasiswa(request, id):
    mhs = Mahasiswa.objects.get(id=id)
    error = ''

    if request.method == 'POST':
        nim = request.POST.get('nim', '').strip()
        nama = request.POST.get('nama', '').strip()
        programstudi = request.POST.get('programstudi', '').strip()

        if not nim or not nama or not programstudi:
            error = 'Harap isi semua field terlebih dahulu.'
            messages.error(request, error)
        else:
            mhs.nim = nim
            mhs.nama = nama
            mhs.programstudi = programstudi
            mhs.save()
            return redirect('daftar_mahasiswa')

    return render(request, 'mahasiswa/edit.html', {
        'mhs': mhs,
        'error': error,
    })


@login_required(login_url='/accounts/login/')
def hapus_mahasiswa(request, id):
    mhs = Mahasiswa.objects.get(id=id)
    mhs.delete()
    return redirect('daftar_mahasiswa')