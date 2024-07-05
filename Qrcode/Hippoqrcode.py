#!/usr/bin/env python3
"""Making a hippo qrcode"""

import qrcode
from PIL import Image

# Créer un QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data('https://www.holbertonschool.fr/')
qr.make(fit=True)

# Créer une image QR Code
img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Charger l'image de l'hippocampe
img_hippocampe = Image.open('Hippo.png')

# Vérifier le mode de l'image et ajuster si nécessaire
if img_hippocampe.mode == 'RGBA':
    # Utiliser le canal alpha comme masque
    mask = img_hippocampe.split()[3]  # Le canal alpha est le 4ème canal dans 'RGBA'
else:
    # Convertir l'image en niveaux de gris pour l'utiliser comme masque
    mask = img_hippocampe.convert('L')

# Redimensionner l'image de l'hippocampe pour qu'elle s'insère dans le QR Code
width, height = img_qr.size
img_hippocampe = img_hippocampe.resize((int(width * 0.5), int(height * 0.5)))
mask = mask.resize((int(width * 0.5), int(height * 0.5)))

# Calculer la position pour centrer l'image de l'hippocampe sur le QR Code
position = ((width - img_hippocampe.width) // 2, (height - img_hippocampe.height) // 2)

# Coller l'hippocampe sur le QR Code en utilisant le masque adapté
img_qr.paste(img_hippocampe, position, mask)

# Sauvegarder l'image finale
img_qr.save('qrcode_hippocampe.png')

# Afficher l'image
img_qr.show()