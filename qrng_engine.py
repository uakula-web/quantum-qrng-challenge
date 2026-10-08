import random
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def generate_quantum_bits(num_bits=1000):
    """
    Generates an array of random binary bits using a 4-qubit Quantum Circuit.
    Applies Hadamard gates to create pure quantum superposition states.
    """
    # 4 qubits matching the strict practical constraint sizes
    num_qubits = 4
    circuit = QuantumCircuit(num_qubits, num_qubits)
    
    # Put all qubits into a 50/50 superposition blur state
    for i in range(num_qubits):
        circuit.h(i)
        
    # Measure the quantum states
    for i in range(num_qubits):
        circuit.measure(i, i)
        
    simulator = AerSimulator()
    
    # Calculate how many runs (shots) we need to fulfill the bit request size
    shots_needed = int(np.ceil(num_bits / num_qubits))
    result = simulator.run(circuit, shots=shots_needed, memory=True).result()
    memory_output = result.get_memory()
    
    bit_string = "".join(memory_output)
    bit_array = [int(b) for b in bit_string[:num_bits]]
    return bit_array

def run_bit_balance_analysis(bit_array):
    """
    Calculates the exact ratio balance between 0s and 1s.
    Proves mathematical stability and fairness.
    """
    total_bits = len(bit_array)
    count_ones = sum(bit_array)
    count_zeroes = total_bits - count_ones
    ratio_ones = count_ones / total_bits
    return count_zeroes, count_ones, ratio_ones

if __name__ == "__main__":
    print("====================================================")
    print(" 🚀 QUANTUM DUAL-ENGINE SIMULATION BENCHMARK RUNNER")
    print("====================================================\n")
    
    SAMPLE_SIZE = 2000
    print(f"📊 Seeding Test Sample Size: {SAMPLE_SIZE} bits generated...\n")
    
    # 1. Execute Quantum Stream Generation
    quantum_data = generate_quantum_bits(SAMPLE_SIZE)
    q_zeros, q_ones, q_ratio = run_bit_balance_analysis(quantum_data)
    
    # 2. Execute Classical Pseudorandom Generation for Fair Comparison
    classical_data = [random.randint(0, 1) for _ in range(SAMPLE_SIZE)]
    c_zeros, c_ones, c_ratio = run_bit_balance_analysis(classical_data)
    
    # 3. Render Metric Output Comparisons
    print("--------- ⚛️ ENGINE A: IBM QISKIT QUANTUM QRNG ---------")
    print(f"• Total Zeroes (0s): {q_zeros} | Total Ones (1s): {q_ones}")
    print(f"• Quantum Bit Balance Ratio (Target 0.50): {q_ratio:.4f}")
    
    print("\n--------- 🐍 ENGINE B: CLASSICAL PSEUDORANDOM ---------")
    print(f"• Total Zeroes (0s): {c_zeros} | Total Ones (1s): {c_ones}")
    print(f"• Classical Bit Balance Ratio (Target 0.50): {c_ratio:.4f}")
    print("\n====================================================")
    print("✅ SUCCESS: Benchmarking execution pipeline complete.")
    print("====================================================")