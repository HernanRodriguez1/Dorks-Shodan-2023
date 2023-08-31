from pynetdicom import AE
from pynetdicom.sop_class import PatientRootQueryRetrieveInformationModelFind
from pydicom import Dataset

ae = AE()

# Specify a requested presentation context
ae.add_requested_context(PatientRootQueryRetrieveInformationModelFind)

ip = "127.0.0.1"
port = 104
association = ae.associate(ip, port)

if association.is_established:
    print('[+] Association established!')

    dataset = Dataset()
    dataset.PatientName = '*'
    dataset.PatientID = ''
    dataset.PatientSex = ''
    dataset.PatientBirthDate = ''
    dataset.StudyDescription = ''
    dataset.QueryRetrieveLevel = "PATIENT"

    results = association.send_c_find(dataset, query_model=PatientRootQueryRetrieveInformationModelFind)

    for (status, dataset) in results:
        if status.Status in (0xFF00, 0xFF01):
            print(dataset)
            print('')

    association.release()



