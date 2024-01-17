from matplotlib import pyplot as plt
import pandas as pd


def get_csv_data_by_name(file_name=None, name=''):
    data = pd.read_csv(file_name)
    result = data[name]
    return result


def show_data(datas, title="Memory data", xlab="second", ylab="Memory data"):
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(datas, c='red')
    plt.title(title, fontsize=24)
    plt.xlabel(xlab, fontsize=24)
    fig.autofmt_xdate()
    plt.ylabel(ylab, fontsize=24)

    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.savefig(title + ".jpg")
    plt.show()


def byte_to_mb(datas):
    for i in range(len(datas)):
        datas[i] = int(datas[i] / 1024 ** 2)
    return datas


if __name__ == '__main__':
    cpu_name = "cpu_percent"
    memory_name = "memory_rss"
    avai_memory = r"memory\Available MBytes"
    file_name = "csv/cpu_memory_usage_20240109140733.csv"
    cpu_data = get_csv_data_by_name(file_name, cpu_name)
    show_data(cpu_data, title="cpu_data", ylab=cpu_name)
    memory_data = get_csv_data_by_name(file_name, memory_name)
    show_data(byte_to_mb(memory_data), title="memory_data", ylab=memory_name + "(MB)")
    avai_memory_data = get_csv_data_by_name(name=avai_memory)
    show_data(avai_memory_data, title="Available_MB", ylab=avai_memory)
