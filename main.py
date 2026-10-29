from smartcard.System import readers


def main():
    print("Windows SIM Card Reader Diagnostics")
    print("-" * 40)

    available_readers = readers()

    if not available_readers:
        print("No smart card readers found.")
        return

    for index, reader in enumerate(available_readers, start=1):
        print(f"\nReader {index}: {reader}")

        connection = None
        try:
            connection = reader.createConnection()
            connection.connect()

            print(f"ATR: {connection.getATR().hex().upper()}")
            print(f"Protocol: {connection.getProtocol()}")

        except Exception as error:
            print(f"Connection information unavailable: {error}")

        finally:
            if connection is not None:
                try:
                    connection.disconnect()
                except Exception:
                    pass


if __name__ == "__main__":
    main()
