INSERT INTO
    work.log (
        "MachineNumber",
        "NumberMachineT",
        "IDEmploye",
        "NumberMachineE",
        "VerifyMode",
        "InOutMode",
        "Date",
        "Time",
        "Warning"
    )
values
    (
        :source,
        :source,
        :worker,
        :source,
        :verify,
        :mode,
        :date,
        :time,
        :remark
    );