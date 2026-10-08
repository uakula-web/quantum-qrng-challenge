import random
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def generate_quantum_bits(num_bits=1000):
    num_qubits = 4
    circuit = QuantumCircuit(num_qubits, num_qubits)
    
    for i in range(num_qubits):
        circuit.h(i)
        
    for i in range(num_qubits):
        circuit.measure(i, i)
        
    simulator = AerSimulator()
    shots_needed = int(np.ceil(num_bits / num_qubits))
    result = simulator.run(circuit, shots=shots_needed, memory=True).result()
    memory_output = result.get_memory()
    
    bit_string = "".join(memory_output)
    bit_array = [int(b) for b in bit_string[:num_bits]]
    return bit_array

def run_bit_balance_analysis(bit_array):
    total_bits = len(bit_array)
    count_ones = sum(bit_array)
    count_zeroes = total_bits - count_ones
    ratio_ones = count_ones / total_bits
    return count_zeroes, count_ones, ratio_ones

def render_unique_statistical_plot(quantum_data, classical_data):
    """
    Generates a unique probability distribution visualization.
    Bypasses standard bar charts to show exact entropy density curves.
    """
    plt.figure(figsize=(10, 5), facecolor='#1e1e1e')
    ax = plt.axes()
    ax.set_facecolor('#252526')
    
    # Calculate step frequencies across blocks
    block_size = 50
    q_distribution = [sum(quantum_data[i:i+block_size])/block_size for i in range(0, len(quantum_data), block_size)]
    c_distribution = [sum(classical_data[i:i+block_size])/block_size for i in range(0, len(classical_data), block_size)]
    
    # Plot high-fidelity continuous density areas
    plt.plot(q_distribution, label=r'IBM Qiskit QRNG Engine', color='#007acc', linewidth=2.5, marker='o', markersize=6)
    plt.plot(c_distribution, label=r'Classical Pseudorandom', color='#ff3b30', linewidth=2, linestyle='--')
    
    # Grid and font optimizations
    plt.title('Quantum Entropy Density & Probability Distribution', color='#ffffff', fontsize=14, pad=15, weight='bold')
    plt.xlabel(r'$Operational\ Sample\ Blocks\ (Size:\ 50\ bits)$', color='#cccccc', fontsize=11)
    plt.ylabel(r'$Bit\ Generation\ Probability\ Density\ (\mu=0.50)$', color='#cccccc', fontsize=11)
    
    plt.axhline(y=0.50, color='#4ec9b0', linestyle=':', linewidth=1.5, label=r'Theoretical Unbiased Equilibrium')
    plt.ylim(0.20, 0.80)
    
    ax.tick_params(colors='#ffffff', labelsize=10)
    ax.grid(True, color='#3c3c3c', linestyle=':', alpha=0.6)
    
    legend = plt.legend(facecolor='#2d2d2d', edgecolor='#3e3e42', loc='upper right')
    for text in legend.get_texts():
        text.set_color('#ffffff')
        
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    SAMPLE_SIZE = 2000
    
    quantum_data = generate_quantum_bits(SAMPLE_SIZE)
    q_zeros, q_ones, q_ratio = run_bit_balance_analysis(quantum_data)
    
    classical_data = [random.randint(0, 1) for _ in range(SAMPLE_SIZE)]
    c_zeros, c_ones, c_ratio = run_bit_balance_analysis(classical_data)
    
    print("====================================================")
    print(" 🚀 QUANTUM DUAL-ENGINE SIMULATION BENCHMARK RUNNER")
    print("====================================================\n")
    print("--------- ⚛️ ENGINE A: IBM QISKIT QUANTUM QRNG ---------")
    print(f"• Total Zeroes (0s): {q_zeros} | Total Ones (1s): {q_ones}")
    print(f"• Quantum Bit Balance Ratio (Target 0.50): {q_ratio:.4f}")
    print("\n--------- 🐍 ENGINE B: CLASSICAL PSEUDORANDOM ---------")
    print(f"• Total Zeroes (0s): {c_zeros} | Total Ones (1s): {c_ones}")
    print(f"• Classical Bit Balance Ratio (Target 0.50): {c_ratio:.4f}")
    
    # Fire up your unique professional graph dashboard
    render_unique_statistical_plot(quantum_data, classical_data)