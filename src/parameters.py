import pathlib as path
import pandas as pd

BASE_DIR = path.Path('.')
DATA_DIR = BASE_DIR / 'data'
OUTPUTS_DIR = BASE_DIR / 'outputs'

ncl_icb = 'QMJ'

performance_metrics = pd.DataFrame({
    'metric' :  ['appts_per_gp',
                'same_day_appointment_percentage',
                'digital_access_percentage',
                'attendance_rate',
                'qof_total',
                'qof_hypertension',
                'qof_child_vaccination',
                'EmergencyPresentationsCancer',
                'AntibioticPrescribing',
                'overallexp',
                'lastgpapptneeds',
                'lastgpapptwait',
                'localgpservicesreception',
                'gpcontactoverall',
                'responsive_coded',
                'overall_coded',
                'wellled_coded',
                'effective_coded',
                'caring_coded',
                'safe_coded'],
    'invert' : [False, False, False, False, False, True, False, True, True, False, False, False, False, False, False, False, False, False, False, False],
    'weight' : [1, 3, 1, 2, 1, 1, 3, 2, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1]
})

column_display_names = {
    'gp_code': 'GP Code',
    'pcn_code': 'PCN Code',
    'icb_code': 'ICB Code',
    'icb_name': 'ICB Name',
    'postcode': 'Postcode',
    'numberofpatients': 'Number of Patients',
    'age': 'Age',
    'responsive': 'Responsive (CQC)',
    'overall': 'Overall (CQC)',
    'wellled': 'Well Led (CQC)',
    'effective': 'Effective (CQC)',
    'caring': 'Caring (CQC)',
    'safe': 'Safe (CQC)',
    'admin_non_clinical': 'Admin Non-Clinical Staff (FTE)',
    'direct_patient_care': 'Direct Patient Care Staff (FTE)',
    'qualified_gp': 'Qualified GPs (FTE)',
    'training_gp': 'Training GPs (FTE)',
    'nurses': 'Nurses (FTE)',
    'PCNWorkforce_FTE': 'PCN Workforce (FTE)',
    'AttendanceOutcome_Attended': 'Attended Appointments',
    'AttendanceOutcome_DNA': 'Missed Appointments',
    'AttendanceOutcome_Unknown': 'Unknown Attendance Appointments',
    'ApptModality_FacetoFace': 'Face to Face Appointments',
    'ApptModality_Telephone': 'Telephone Appointments',
    'BookingtoApptGap_1Day': 'Booking to Appointment Gap - 1 Day',
    'BookingtoApptGap_2to7Days': 'Booking to Appointment Gap - 2 to 7 Days',
    'BookingtoApptGap_8to14Days': 'Booking to Appointment Gap - 8 to 14 Days',
    'BookingtoApptGap_15to21Days': 'Booking to Appointment Gap - 15 to 21 Days',
    'BookingtoApptGap_22to28Days': 'Booking to Appointment Gap - 22 to 28 Days',
    'BookingtoApptGap_Morethan28Days': 'Booking to Appointment Gap - More than 28 Days',
    'BookingtoApptGap_UnknownDataIssue': 'Booking to Appointment Gap - Unknown Data Issue',
    'overallexp': 'Overall Experience (GP Survey)',
    'lastgpapptneeds': 'Last GP Appointment Needs Met (GP Survey)',
    'lastgpapptwait': 'Last GP Appointment Waiting Time (GP Survey)',
    'localgpservicesreception': 'Reception Helpfullness (GP Survey)',
    'gpcontactoverall': 'Last Contact Experience (GP Survey)',
    'IMD2019': 'IMD 2019',
    'Total_QoF': 'QoF Total',
    'Hypertension': 'QoF Hypertension',
    'EmergencyPresentationsCancer': 'QoF Emergency Presentations Cancer',
    'BreastScreeningCancer': 'QoF Breast Screening Cancer',
    'ChildVaccination': 'QoF Child Vaccination',
    'AntibioticPrescribing': 'QoF Antibiotic Prescribing'
}