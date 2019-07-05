null = None
true = True
false = False

d = {
  "loan_officer_count": 6,
  "appraiser_count": 7,
  "average_turn_time": 2.7,
  "ratio_revisions": 0.1,
  "unassigned_orders": [
    {
      "id": "5d1397896ad88b00344c4b40",
      "status": "Finding Appraisers",
      "statusKey": "finding_appraisers",
      "on_hold": false,
      "number": "Jun2601",
      "address": "432 D St",
      "city": "Boston",
      "state": "MA",
      "appraiser_requested_cancel": false,
      "due_date": "2019-07-04 12:00:00",
      "accepted": null,
      "created": "2019-06-26 16:04:25.394000",
      "lender_canceled": false,
      "unreplied_message": false,
      "lender_attention_required": true,
      "inspection_complete": false,
      "job_type": "manually",
      "is_report_approved": null,
      "client_name": "",
      "loan_file": {
        "id": "5d1397406ad88b00344c4b3f",
        "rush": false,
        "number": "Jun2601",
        "officer": {
          "id": "32879438704398343948",
          "username": null,
          "email": "test@test.com",
          "phone_number": "1231231234",
          "cell_number": null,
          "is_review_appraiser": false,
          "firstname": "Trisha",
          "lastname": "lo1",
          "nmls_id": "",
          "lender": {
            "id": "32879438704398343948",
            "name": "Trisha Lender One",
            "time_limit": "0.04",
            "rush_time_limit": "1.0",
            "automatic_weighting_method": "manual",
            "automatic_manual_weights": {
              "32879438704398343948": 0,
              "32879438704398343948": 100
            },
            "send_appraiser_invoice": false,
            "send_borrower_appraisal": false,
            "appraiser_invoice_format": "generation",
            "calendar_type": "business",
            "blacklist": [
              {
                "appraiser": {
                  "id": "32879438704398343948",
                  "firm_name": "Trish Appraiser Firm2",
                  "lender_owner": "32879438704398343948",
                  "name": "Taylor Swift",
                  "email": "tes@tes32879438704398343948.com",
                  "phone": "1231231234",
                  "is_blacklisted": true,
                  "blacklist_reason": "k",
                  "is_deleted": false,
                  "company": "32879438704398343948",
                  "accepting_jobs": true,
                  "not_accepting_jobs_reason": null,
                  "lender_coverage": [],
                  "company_is_shell": false,
                  "created": "2019-05-29 12:49:31.199000"
                },
                "message": "k"
              }
            ],
            "address": "7 Reggora St",
            "city": "ReggoraLand",
            "zip": "18003",
            "email": "z@test.com",
            "default_files": [],
            "merchant": null,
            "stripe": "acct_1EkAasfyoK7yaasdUZYGQKL",
            "stripe_payments_enabled": true,
            "auto_send_payment": true,
            "wait_for_payment": true,
            "email_name": "Trisha's Test Bank",
            "email_text": "",
            "delivery_email_text": "Here is your completed appraisal",
            "email_logo": "https://google.com",
            "custom_settings": {
              "evault_filename": true
            },
            "loan_csv_mapping": {
              "Co-Borr Home Phone": "Sellers Agent Phone",
              "Sellers Agent E-mail": "Sellers Agent E-mail",
              "Borr Cell": "Borr Cell",
              "Borr Home Phone": "Borr Home Phone",
              "BORR BUSINESS PHONE": "Borr Business Phone",
              "BORR EMAIL": "Borr Email"
            },
            "loan_csv_custom_fields": ["Loan Purpose other"],
            "additional_notes": [
              {
                "id": "e25casde062-238e-4cbeads-b9d75-7e73fbead890",
                "note": "twoasdfasdf",
                "timestamp": "2019-04-11 12:59:30.723000"
              }
            ],
            "is_amc_lender": false,
            "is_using_amc": null,
            "custom_panel": null,
            "use_internal_email": true,
            "internal_email": "test@test.com",
            "use_internal_email_valuation": false,
            "internal_email_valuation": null,
            "default_allocation_mode": "automatically",
            "default_due_date": 0,
            "default_due_date_internal": 6,
            "default_due_date_internal_rush": 5,
            "use_default_rush_fee": true,
            "default_rush_fee": 12,
            "ucdp_business_unit_number": "341234231325",
            "ead_business_unit_number": "12351235135151",
            "fha_lender_id": "",
            "fnm_seller_number": "543523453425",
            "fre_identification_number": "",
            "enable_email_response": true,
            "daily_email_time_hour": "12",
            "daily_email_time_minute": "00",
            "is_authorize_enabled": null,
            "integration_user": "32879438704398343948",
            "stripe_payment_method": {
              "manually": "reggora_direct",
              "automatically": "reggora_direct",
              "amc": "reggora_direct"
            },
            "should_show_consumer_payment_style_field": true
          },
          "settings": {
            "match_loan_officers": false,
            "officers": []
          },
          "matched_users": [],
          "created": "2019-05-29 13:11:22.901000",
          "is_demo": false,
          "role": {
            "id": "32879438704398343948",
            "name": "Loan Officer",
            "permissions": {
              "order_access_all": {
                "readable": "Access all orders in your lender",
                "allowed": false,
                "group_by": "Order Access"
              },
              "order_access_assigned": {
                "readable": "Access orders you are assigned to",
                "allowed": true,
                "group_by": "Order Access"
              }
            },
            "notification_settings": {
              "status_change": false,
              "order_message": false,
              "report_delivery": false,
              "inspection_scheduled": false,
              "report_completed": false,
              "inspection_completed": false,
              "payment_complete": false,
              "appraiser_license_expiration": false,
              "order_company_assignment_decline": false,
              "consumer_submission_download_alerts": false,
              "order_behind_schedule": false,
              "order_note_created": false,
              "requires_lender_attention": false,
              "order_cancel_request": false,
              "evault_upload": false
            }
          },
          "is_removed": false,
          "branch": null,
          "branches": [],
          "zones": [],
          "suppress_notifications": true,
          "text_notifications": false,
          "email_notifications": true,
          "scheduled_reports": []
        },
        "appraisal_type": "purchase",
        "consumers": [],
        "due_date": "2019-07-04 12:00:00",
        "lender": {
          "id": "32879438704398343948",
          "name": "Trisha Lender One",
          "time_limit": "0.04",
          "rush_time_limit": "1.0",
          "address": "7 Reggora St",
          "city": "ReggoraLand",
          "zip": "18003",
          "email": "z@zippiex.com",
          "ucdp_business_unit_number": "341234231325",
          "ead_business_unit_number": "12351235135151",
          "fha_lender_id": "",
          "fnm_seller_number": "543523453425",
          "fre_identification_number": ""
        },
        "subject_property_address": "432 D St",
        "subject_property_city": "Boston",
        "subject_property_state": "MA",
        "subject_property_zip": "02210",
        "subject_property_type": null,
        "created": "2019-06-26 16:03:11.999000",
        "updated": "2019-06-26 16:03:11.999000",
        "electronic_consent": null,
        "ucdp_submissions": [],
        "consumer_payment_style": "ordering"
      },
      "is_follow_up": null,
      "primary_order_id": null
    }
  ],
  "incomplete_orders": [
    {
      "id": "32879438704398343948",
      "status": "Finding Appraisers",
      "statusKey": "finding_appraisers",
      "on_hold": false,
      "number": "627A",
      "address": "86 Newbury St",
      "city": "Boston",
      "state": "MA",
      "appraiser_requested_cancel": false,
      "due_date": "2019-07-20 12:00:00",
      "accepted": {
        "id": "32879438704398343948",
        "firm_name": "Trish Appraiser Firm3",
        "accepting_jobs": true,
        "company": "32879438704398343948",
        "email": "test@test.com",
        "phone": "1231231234"
      },
      "created": "2019-06-27 14:22:21.794000",
      "lender_canceled": false,
      "unreplied_message": false,
      "lender_attention_required": false,
      "inspection_complete": false,
      "job_type": "automatically",
      "is_report_approved": null,
      "client_name": "Bo Rower",
      "loan_file": {
        "id": "32879438704398343948",
        "rush": false,
        "number": "627A",
        "officer": null,
        "appraisal_type": "Purchase",
        "consumers": [
          {
            "id": "190209f2-3e9a-401f-82de-e2cd33c13ab0",
            "full_name": "Bo Rower",
            "firstname": null,
            "lastname": null,
            "role": "borrower",
            "email": "trisha+borrower@reggora.com",
            "address": null,
            "home_phone": "857-231-3620",
            "work_phone": "857-231-3620",
            "cell_phone": "857-231-3620",
            "schedule_sent": [],
            "payment_sent": [],
            "report_sent": null,
            "electronic_consent": null,
            "report_downloaded": null,
            "denied_electronic_consent": null,
            "hidden": null
          }
        ],
        "due_date": "2019-07-20 12:00:00",
        "lender": {
          "id": "32879438704398343948",
          "name": "Trisha Lender One",
          "time_limit": "0.04",
          "rush_time_limit": "1.0",
          "address": "7 Reggora St",
          "city": "ReggoraLand",
          "zip": "18003",
          "email": "test@test.com",
          "ucdp_business_unit_number": "341234231325",
          "ead_business_unit_number": "12351235135151",
          "fha_lender_id": "",
          "fnm_seller_number": "543523453425",
          "fre_identification_number": ""
        },
        "subject_property_address": "86 Newbury St",
        "subject_property_city": "Boston",
        "subject_property_state": "MA",
        "subject_property_zip": "02116",
        "subject_property_type": "Single Family",
        "created": "2019-06-27 14:14:21.311000",
        "updated": "None",
        "electronic_consent": false,
        "ucdp_submissions": [],
        "consumer_payment_style": "ordering"
      },
      "is_follow_up": null,
      "primary_order_id": null
    }
  ]
}

d2 = {
    "a": {
        "a1": { 
            "a2": [ 1, 2, 3],
            "b2": {
                "a3": [
                    { 
                        "a4": True,
                        "b4": [ "i", "am", "string"]
                    }
                ],
                "b3": 123
            }
        }, 
    },
    "b": [
            {},
            {}
        ],
    "c": [1,2,3, 'str', False ],
    "d": True
}

d3 = {
    "a": {
        "a1": { 
            "a2": [ 1, 2, 3],
            "b2": {
                "a3": [
                    { 
                        "a4": True,
                        "b4": [ "i", "am", "string"]
                    }
                ],
                "b3": 123
            }
        }, 
    },
    "b": [
            {
                "ba2": [],
                "bb2": {
                    "ba3": [],
                    "bb3": [ 1, 2, 3, False ]
                }
            }
        ],
    "c": [1,2,3, 'stuff', False ],
    "d": True
}

def recursive_print(data, dpth = 0, key = ''):
    """ Recursively prints data types of nested elements"""
    tabs = lambda n: ' ' * n * 2 
    if isinstance(data, dict):
        print(tabs(dpth) + '\x1b[0;33;40m { \x1b[0m')
        for key, value in data.items():
            print(tabs(dpth+1) + key + ': ' + value.__class__.__name__ + ',' )
            recursive_print(value, dpth + 1, key)
        print(tabs(dpth) + '\x1b[0;33;40m } \x1b[0m')
    elif isinstance(data, list):
        print(tabs(dpth) + '\x1b[0;35;40m', '[', '\x1b[0m')
        for litem in data:
            recursive_print(litem, dpth + 2)
        print(tabs(dpth) + '\x1b[0;35;40m', ']', '\x1b[0m')
    else:
        if key:
            pass
        else:
            print(tabs(dpth) + '%s - %s, depth: %s ' % (data, data.__class__.__name__, dpth))

val = recursive_print(d)

# expected = recursive_print(d2)
# response = recursive_print(d3)