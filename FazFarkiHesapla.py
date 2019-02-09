#numpy load et
import numpy as np
import os

print("Dosyalar inceleniyor...")
almac_dosya = "/home/murat/git/murat-sever/gr-work/fft_yon_sim_10Mcenter_30degree.bin"
boyut = os.path.getsize(almac_dosya)
frame_sayisi = boyut / (8*96*8)
# kanal0
kanal0_faz_sayisi = os.path.getsize("/home/murat/git/murat-sever/gr-work/output_binaries/faz0.bin") /4
if frame_sayisi != kanal0_faz_sayisi:
    print("hata")
    
# kanal1
kanal1_faz_sayisi = os.path.getsize("/home/murat/git/murat-sever/gr-work/output_binaries/faz1.bin") /4
if frame_sayisi != kanal1_faz_sayisi:
    print("hata")

#dosyadan float32 olarak oku
fft0_f=np.fromfile('/home/murat/git/murat-sever/gr-work/output_binaries/fft0.bin', 'float32', -1, '')
#real interleaved to complex donusum icin
#yani cift degerler (real) + tek degerler (imag)
fft0_cf = fft0_f[::2]+1j*fft0_f[1::2]

genlik0_f=np.fromfile('/home/murat/git/murat-sever/gr-work/output_binaries/genlik0.bin', 'float32', -1, '')
faz0_f=np.fromfile('/home/murat/git/murat-sever/gr-work/output_binaries/faz0.bin', 'float32', -1, '')

genlik1_f=np.fromfile('/home/murat/git/murat-sever/gr-work/output_binaries/genlik1.bin', 'float32', -1, '')
faz1_f=np.fromfile('/home/murat/git/murat-sever/gr-work/output_binaries/faz1.bin', 'float32', -1, '')

fazfarki1_f=np.fromfile('/home/murat/git/murat-sever/gr-work/output_binaries/fazfarki_0_1.bin', 'float32', -1, '')
fazfarki1_cf = fazfarki1_f[::2]+1j*fazfarki1_f[1::2]
fazfarki1 = np.angle(fazfarki1_cf)
fazfarki1 = (fazfarki1 + 2 * np.pi) % (2 * np.pi)

fazfarki2_f=np.fromfile('/home/murat/git/murat-sever/gr-work/output_binaries/fazfarki_0_2.bin', 'float32', -1, '')
fazfarki2_cf = fazfarki2_f[::2]+1j*fazfarki2_f[1::2]
fazfarki2 = np.angle(fazfarki2_cf)
fazfarki2 = (fazfarki2 + 2 * np.pi) % (2 * np.pi)

fazfarki3_f=np.fromfile('/home/murat/git/murat-sever/gr-work/output_binaries/fazfarki_0_3.bin', 'float32', -1, '')
fazfarki3_cf = fazfarki3_f[::2]+1j*fazfarki3_f[1::2]
fazfarki3 = np.angle(fazfarki3_cf)
fazfarki3 = (fazfarki3 + 2 * np.pi) % (2 * np.pi)

fazfarki4_f=np.fromfile('/home/murat/git/murat-sever/gr-work/output_binaries/fazfarki_0_4.bin', 'float32', -1, '')
fazfarki4_cf = fazfarki4_f[::2]+1j*fazfarki4_f[1::2]
fazfarki4 = np.angle(fazfarki4_cf)
fazfarki4 = (fazfarki4 + 2 * np.pi) % (2 * np.pi)

fazfarki5_f=np.fromfile('/home/murat/git/murat-sever/gr-work/output_binaries/fazfarki_0_5.bin', 'float32', -1, '')
fazfarki5_cf = fazfarki5_f[::2]+1j*fazfarki5_f[1::2]
fazfarki5 = np.angle(fazfarki5_cf)
fazfarki5 = (fazfarki5 + 2 * np.pi) % (2 * np.pi)

fazfarki6_f=np.fromfile('/home/murat/git/murat-sever/gr-work/output_binaries/fazfarki_0_6.bin', 'float32', -1, '')
fazfarki6_cf = fazfarki6_f[::2]+1j*fazfarki6_f[1::2]
fazfarki6 = np.angle(fazfarki6_cf)
fazfarki6 = (fazfarki6 + 2 * np.pi) % (2 * np.pi)

fazfarki7_f=np.fromfile('/home/murat/git/murat-sever/gr-work/output_binaries/fazfarki_0_7.bin', 'float32', -1, '')
fazfarki7_cf = fazfarki7_f[::2]+1j*fazfarki7_f[1::2]
fazfarki7 = np.angle(fazfarki7_cf)
fazfarki7 = (fazfarki7 + 2 * np.pi) % (2 * np.pi)

#faz icin
print(np.angle(fft0_cf[38]))
print(faz0_f[0])

#genlik
print(abs(fft0_cf[38]))
print(genlik0_f[0])

print(np.unwrap(faz1_f - faz0_f))

print("Kanal0-1 faz farki")
print(np.rad2deg(fazfarki1))
print("Kanal0-2 faz farki")
print((np.rad2deg(fazfarki2)))
print("Kanal0-3 faz farki")
print((np.rad2deg(fazfarki3)))
print("Kanal0-4 faz farki")
print((np.rad2deg(fazfarki4)))
print("Kanal0-5 faz farki")
print((np.rad2deg(fazfarki5)))
print("Kanal0-6 faz farki")
print((np.rad2deg(fazfarki6)))
print("Kanal0-7 faz farki")
print((np.rad2deg(fazfarki7)))

print("son")
