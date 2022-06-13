# pg_sbs-pygame-sub-pixel-surface-
clean-up and adaptation of https://www.willmcgugan.com/blog/tech/post/going-sub-pixel-with-pygame/ for python3 with Numpy.
Both this and the original code are public domain.

To use it in your code, replace: 
    screen.blit(some_surface, (x, y))
by: 
    some_surface_subpixel = SubPixelSurface(some_surface) 
    screen.blit(some_surface_subpixel.at(x, y), (x, y)) 
of course, take care to not re-create the SubPixelSurface every frame.
