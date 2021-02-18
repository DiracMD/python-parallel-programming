from mpi4py import MPI

comm=MPI.COMM_WORLD
rank=commfrom mpi4py import MPI

comm=MPI.COMM_WORLD
rank=comm.Get_rank()

if rank==0:
    data={"a":7,"b":3.14}
    print("")
