"""
Aerospace Wing Box FEA Post-Processing & Convergence Engine
Author: Muhammad Yousuf Baig
Description: Automates convergence plotting and material trade-off visualization from FEA logs.
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_spatial_convergence():
    # Mesh element sizes (Coarse, Medium, Fine)
    mesh_sizes = np.array([0.10, 0.05, 0.01])
    mesh_labels = ['Coarse\n(0.10 m)', 'Medium\n(0.05 m)', 'Fine\n(0.01 m)']
    
    # Displacement USUM (m) from ANSYS APDL logs
    disp_wing_up = np.array([0.004464, 0.004567, 0.004657])
    disp_wing_down = np.array([0.001918, 0.001944, 0.002017])
    
    fig, ax1 = plt.subplots(figsize=(8, 5))
    
    # Plot Displacement Convergence
    ax1.plot(mesh_labels, disp_wing_up * 1e3, marker='o', color='#d63031', linewidth=2, label='Wing-Up (+g Maneuver)')
    ax1.plot(mesh_labels, disp_wing_down * 1e3, marker='s', color='#0984e3', linewidth=2, label='Wing-Down (-g Maneuver)')
    
    ax1.set_title('Spatial Grid Convergence: Tip Deflection vs. Mesh Density', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Mesh Density Level', fontsize=11)
    ax1.set_ylabel('Peak Vector Displacement USUM [mm]', fontsize=11)
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.legend(loc='center right', frameon=True)
    
    plt.tight_layout()
    plt.savefig('mesh_convergence_curve.png', dpi=300)
    print("Generated: mesh_convergence_curve.png")

def plot_material_scaling():
    materials = ['Al 2024-T3', 'Al 7075-T6', 'Ti-6Al-4V']
    yield_strength = [345, 503, 880]       # MPa
    total_cost_m = [8.51, 6.82, 47.26]     # Million USD
    
    x = np.arange(len(materials))
    width = 0.35
    
    fig, ax1 = plt.subplots(figsize=(8, 5))
    ax2 = ax1.twinx()
    
    rects1 = ax1.bar(x - width/2, yield_strength, width, label='Yield Strength (MPa)', color='#2d3436')
    rects2 = ax2.bar(x + width/2, total_cost_m, width, label='Total Cost ($M)', color='#e17055')
    
    ax1.set_xlabel('Aerospace Alloy', fontsize=11)
    ax1.set_ylabel('Yield Strength [MPa]', color='#2d3436', fontsize=11)
    ax2.set_ylabel('Total Structural Cost [Million USD]', color='#e17055', fontsize=11)
    ax1.set_xticks(x)
    ax1.set_xticklabels(materials)
    ax1.set_title('Techno-Economic Material Trade-Off Analysis', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('material_tradeoff_scaling.png', dpi=300)
    print("Generated: material_tradeoff_scaling.png")

if __name__ == '__main__':
    plot_spatial_convergence()
    plot_material_scaling()
