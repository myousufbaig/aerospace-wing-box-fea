# Visual Analysis and APDL Post-Processing

This directory contains the visual results generated from the ANSYS APDL `/POST1` post-processing stage. It includes mesh comparisons, stress contours, displacement plots, and modal deformation results.

## Directory Structure

- **`/mesh_comparison`**  
  Contains images comparing the three mesh sizes:
  - Coarse: 0.10 m
  - Medium: 0.05 m
  - Fine: 0.01 m

  The plots show the difference in mesh density and spatial discretization.

- **`/stress_plots`**  
  Contains von Mises equivalent stress contours for the wing box. The plots show the stress distribution, areas of higher stress near the wing root, and the relationship between the calculated stress and the material yield strength.

- **`/displacement_plots`**  
  Contains total displacement (`USUM`) contours showing the deformation of the wing box under positive and negative aerodynamic loading. The results show the bending and torsional deformation of the structure.

- **`/modal_results`**  
  Contains the deformation shapes from the Block Lanczos modal analysis. The results show the primary and higher-order bending and torsional vibration modes of the wing box.
