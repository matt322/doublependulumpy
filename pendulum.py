import numpy as np
import pygame

# pendulum vars
L0, L1 = 1,1 #length
m0, m1 = 1,1 #mass
g = 10 #grav constant
mu = 0 #coefficient of friction
tstep = 0.0007 #time step for differential
theta0, theta1 = 2, 2 #inital angle theta
theta_prime0, theta_prime1 = 0, 0 #initial angular velocity
orig = (360, 250) #pendulum origin

def theta_double_prime_0(theta0, theta_prime0, theta1, theta_prime1):
  return (-g*(2*m0+m1)*np.sin(theta0)-m1*g*np.sin(theta0-2*theta1)-2*np.sin(theta0-theta1)*m1*(theta_prime1**2*L1+theta_prime0**2*L0*np.cos(theta0-theta1)))/(L0*(2*m0+m1-m1*np.cos(2*theta0-2*theta1))) -mu*theta_prime0


def theta_double_prime_1(theta0, theta_prime0, theta1, theta_prime1):
  return (2*np.sin(theta0-theta1)*(theta_prime0**2*L0*(m0+m1)+g*(m0+m1)*np.cos(theta0)+theta_prime1**2*L1*m1*np.cos(theta0-theta1)))/(L1*(2*m0+m1-m1*np.cos(2*theta0-2*theta1))) -mu*theta_prime1

def endpoint(theta, x, y):
  return ((int(170*np.sin(theta)+x), int(170*np.cos(theta)+y)))

screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption('Pendulum')
screen.fill((255,255,255))
pygame.display.flip()
running = True

trailscreen = pygame.Surface((720, 720))
trailscreen.fill((255,255,255))



while running:
  e0 = endpoint(theta0, orig[0], orig[1])
  e1 = endpoint(theta1, e0[0], e0[1])
  trailscreen.set_at(e1, (0,0,255))
  screen.blit(trailscreen, (0,0))
  pygame.draw.line(screen, (0,0,0), orig, e0, 2)
  pygame.draw.line(screen, (0,0,0), e0, e1, 2)
  pygame.draw.circle(screen, (0,100,0), e0, 20) 
  pygame.draw.circle(screen, (0,100,0), e1, 20)
  pygame.display.flip()
  
  theta0 += theta_prime0 * tstep
  theta_prime0 += theta_double_prime_0(theta0, theta_prime0, theta1, theta_prime1) * tstep
  theta1 += theta_prime1 * tstep
  theta_prime1 += theta_double_prime_1(theta0, theta_prime0, theta1, theta_prime1) * tstep
  screen.fill((255,255,255))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False    


