### FLAGS

- bin_identifyer, STRING used for identifing bin, location and persons attatched.

- [time_stamp], time for data proped

- [bin_level], how filed the bin is from 0 - 100, in procent.

- [last_emptyed], time since the bin was last emptyed.

- [contains_meat], bool value, if the bin contains meat

- [append_dangerous_trash], bool value, if a bin with dangerous trash also needs to be collected.

### EXAMPLE CSV

| bin_identifyer | time_stamp          | bin_level | last_emptyed | contains_meat | append_dangerous_trash |
| -------------- | ------------------- | --------- | ------------ | ------------- | ---------------------- |
| BIN001         | 2025-03-17 08:30:00 | 75        | 2025-03-15   | true          | false                  |
| BIN002         | 2025-03-17 09:15:00 | 40        | 2025-03-14   | false         | false                  |
| BIN003         | 2025-03-17 10:00:00 | 90        | 2025-03-12   | true          | true                   |
| BIN004         | 2025-03-17 11:45:00 | 20        | 2025-03-16   | false         | false                  |
| BIN005         | 2025-03-17 12:30:00 | 55        | 2025-03-15   | false         | true                   |
| BIN006         | 2025-03-17 13:10:00 | 85        | 2025-03-13   | true          | false                  |
| BIN007         | 2025-03-17 14:00:00 | 30        | 2025-03-16   | false         | false                  |
| BIN008         | 2025-03-17 14:45:00 | 95        | 2025-03-11   | true          | true                   |
| BIN009         | 2025-03-17 15:20:00 | 10        | 2025-03-17   | false         | false                  |
| BIN010         | 2025-03-17 16:00:00 | 60        | 2025-03-14   | false         | true                   |
