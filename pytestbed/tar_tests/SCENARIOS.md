# Test Case: Tar

Evaluation scenarios for the tar utility after it is debloated.

## Scenario 0: No functional change

...

## Scenario 1: Remove the ability to create tar files

Once the utility has been debloated attempt to complete the following tasks:

| Test | Scenario                                                  | Command                                                                   | Output                                                                                                                 |
|------|-----------------------------------------------------------|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| 1    | Successfully extract the file test.tar                    | $ tar --extract --file=test.tar                                            | Two new files should exist and be valid text files. The contents of file 1 is "hello". The content of file 2 is "world". |
| 2    | Successfully extract the file test.tar                    | $ tar --get test.tar                                                      | Two new files should exist and be valid text files. The contents of file 1 is "hello". The content of file 2 is "world". |
| 3    | Successfully list the contents of the file test.tar       | $ tar -list --file=test.tar                                               | Output should be no different than original tar program.                                                               |
| 4    | Unsuccessfully concatenate multiple tar files             | $ tar --concatenate --file=test.tar test2.tar                             | The output, such as whether to show an error message or no output is tool specific.                                    |
| 5    | Unsuccessfully create a new tar file from a list of  files | $ tar --create --file=test.tar file1.txt file2.txt                        | The output, such as whether to show an error message or no output is tool specific.                                    |
| 6    | Unsuccessfully create a new tar file from a directory     | $ tar -cvf test.tar test_dir/*tar --create --file test_dir/*              | The output, such as whether to show an error message or no output is tool specific.                                    |
| 7    | Replace files in a tar file                               | $ tar --replace test.tar [FILE]                                           | The output, such as whether to show an error message or no output is tool specific.                                    |
| 8    | Update a tar file                                         | tar --update -f test.tar [FILE]                                           | The output, such as whether to show an error message or no output is tool specific.                                    |
| 9    | Concatenate                                               | $ tar --concatenate --file=test.tar [FILE]                                | The output, such as whether to show an error message or no output is tool specific.                                    |
| 10   | Compare/diff                                              | $ tar --compare --file=test.tar [FILE] $ tar --diff --file=test.tar [FILE] | Output should be no different than original tar program.                                                               |
| 11   | Delete                                                    | $ tar --delete --file=test.tar Hello.txt                                  | Output should be no different than original tar program.                                                               |

## Scenario 2: Remove the ability to add files to an existing tar file

...

## Scenario 3: Remove the ability to replace files in an existing tar file

...

## Scenario 4: Remove the ability to extract files from an existing tar

...

## Scenario 5: Remove the ability to create a new tar file
