from codecarbon import EmissionsTracker, OfflineEmissionsTracker, track_emissions
tracker = OfflineEmissionsTracker(country_iso_code="IND")

@track_emissions(project_name="green")
def cal(n):
    for i in range(n):
        x=1


if __name__ == "__main__":
    # tracker.start()
    cal(10**8)
    # tracker.stop()