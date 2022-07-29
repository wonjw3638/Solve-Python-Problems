N=int(input())

def stars(N):
  if N == 1:
    return '*'

  image = []
    
  for star in stars(N // 3):
    image.append(star *3)

  for star in stars(N // 3):
    image.append(star + ' ' * (N // 3) + star)

  for star in stars(N // 3):
    image.append(star * 3)

  return image

print('\n'.join(stars(N)))