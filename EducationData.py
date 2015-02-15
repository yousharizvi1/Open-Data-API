# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# Base = declarative_base()
# engine = create_engine('postgresql://ashar:ashar@localhost:5432/open_data', echo=True)
#
# class EducationData(Base):
#
#     __tablename__ = 'education_data'
#
#     id = Column(Integer, primary_key=True)
#     country = Column(String)
#     province_or_territory = Column(String)
#     district_or_agency = Column(String)
#     region_type = Column(String)
#     date = Column(String)
#     urban_male_population_that_has_ever_attended_school = Column(Integer)
#     urban_female_population_that_has_ever_attended_school = Column(Integer)
#     total_urban_population_that_has_ever_attended_school = Column(Integer)
#     rural_male_population_that_has_ever_attended_school = Column(Integer)
#     rural_female_population_that_has_ever_attended_school = Column(Integer)
#     total_rural_population_that_has_ever_attended_school = Column(Integer)
#     total_male_population_that_has_ever_attended_school = Column(Integer)
#     total_female_population_that_has_ever_attended_school = Column(Integer)
#     total_population_that_has_ever_attended_school = Column(Integer)
#     percentage_distribution_of_urban_male_population_that_at_least_completed_primary_level = Column(Integer)
#     percentage_distribution_of_urban_female_population_that_at_least_completed_primary_level = Column(Integer)
#     percentage_distribution_of_total_urban_population_that_at_least_completed_primary_level = Column(Integer)
#     percentage_distribution_of_rural_male_population_that_at_least_completed_primary_level = Column(Integer)
#     percentage_distribution_of_rural_female_population_that_at_least_completed_primary_level = Column(Integer)
#     percentage_distribution_of_total_rural_population_that_at_least_completed_primary_level = Column(Integer)
#     percentage_distribution_of_total_male_population_that_at_least_completed_primary_level = Column(Integer)
#     percentage_distribution_of_total_female_population_that_at_least_completed_primary_level = Column(Integer)
#     percentage_distribution_of_total_population_that_at_least_completed_primary_level = Column(Integer)
#     urban_male_gross_enrolment_rate_primary__age_5_9___excluding_katchi_class_ = Column(Integer)
#     urban_female_gross_enrolment_rate_primary_level__age_5_9___excluding_katchi_class_ = Column(Integer)
#     total_urban_gross_enrolment_rate__primary_level__age_5_9___excluding_katchi_class_ = Column(Integer)
#     rural_male_gross_enrolment_rate_primary_level__age_5_9___excluding_katchi_class_ = Column(Integer)
#     rural_female_gross_enrolment_rate_primary_level__age_5_9___excluding_katchi_class_ = Column(Integer)
#     total_rural_gross_enrolment_rate_primary_level__age_5_9___excluding_katchi_class_ = Column(Integer)
#     total_male_gross_enrolment_rate_primary_level__age_5_9___excluding_katchi_class_ = Column(Integer)
#     total_female_gross_enrolment_rate__primary_level__age_5_9___excluding_katchi_class_ = Column(Integer)
#     total_gross_enrolment_rate_primary_level__age_5_9___excluding_katchi_class_ = Column(Integer)
#     urban_male_gross_enrolment_rate_primary_level__age_6_10___excluding_katchi_class_ = Column(Integer)
#     urban_female_gross_enrolment_rate_primary_level__age_6_10___excluding_katchi_class_ = Column(Integer)
#     total_urban_gross_enrolment_rate_primary_level__age_6_10___excluding_katchi_class_ = Column(Integer)
#     rural_male_gross_enrolment_rate_primary_level__age_6_10___excluding_katchi_class_ = Column(Integer)
#     rural_female_gross_enrolment_rate_primary_level__age_6_10___excluding_katchi_class_ = Column(Integer)
#     total_rural_gross_enrolment_rate_primary_level__age_6_10___excluding_katchi_class_ = Column(Integer)
#     total_male_gross_enrolment_rate_primary_level__age_6_10___excluding_katchi_class_ = Column(Integer)
#     total_female_gross_enrolment_rate_primary_level__age_6_10___excluding_katchi_class_ = Column(Integer)
#     total_gross_enrolment_rate_primary_level__age_6_10___excluding_katchi_class_ = Column(Integer)
#     urban_male_gross_enrolment_rate_primary_level__age_4_9___including_katchi_class_ = Column(Integer)
#     urban_female_gross_enrolment_rate_primary_level__age_4_9___including_katchi_class_ = Column(Integer)
#     total_urban_gross_enrolment_rate_primary_level__age_4_9___including_katchi_class_ = Column(Integer)
#     rural_male_gross_enrolment_rate_primary_level__age_4_9___including_katchi_class_ = Column(Integer)
#     rural_female_gross_enrolment_rate_primary_level__age_4_9___including_katchi_class_ = Column(Integer)
#     total_rural_gross_enrolment_rate_primary_level__age_4_9___including_katchi_class_ = Column(Integer)
#     total_male_gross_enrolment_rate_primary_level__age_4_9___including_katchi_class_ = Column(Integer)
#     total_female_gross_enrolment_rate_primary_level__age_4_9___including_katchi_class_ = Column(Integer)
#     total_gross_enrolment_rate_primary_level__age_4_9___including_katchi_class_ = Column(Integer)
#     urban_male_gross_enrolment_rate_for_government_primary_schools__age_5_9___excluding_katchi_class_ = Column(Integer)
#     urban_female_gross_enrolment_rate_for_government_primary_schools__age_5_9___excluding_katchi_class_ = Column(Integer)
#     total_urban_gross_enrolment_rate_for_government_primary_schools__age_5_9___excluding_katchi_class_ = Column(Integer)
#     rural_male_gross_enrolment_rate_for_government_primary_schools__age_5_9___excluding_katchi_class_ = Column(Integer)
#     rural_female_gross_enrolment_rate_for_government_primary_schools__age_5_9___excluding_katchi_class_ = Column(Integer)
#     total_rural_gross_enrolment_rate_for_government_primary_schools__age_5_9___excluding_katchi_class_ = Column(Integer)
#     total_male_gross_enrolment_rate_for_government_primary_schools__age_5_9___excluding_katchi_class_ = Column(Integer)
#     total_female_gross_enrolment_rate_for_government_primary_schools__age_5_9___excluding_katchi_class_ = Column(Integer)
#     total_gross_enrolment_rate_for_government_primary_schools__age_5_9___excluding_katchi_class_ = Column(Integer)
#     urban_male_net_enrolment_rate_primary_level__age_5_9___excluding_katchi_class_ = Column(Integer)
#     urban_female_net_enrolment_rate_primary_level__age_5_9___excluding_katchi_class_ = Column(Integer)
#     total_urban_net_enrolment_rate_primary_level__age_5_9___excluding_katchi_class_ = Column(Integer)
#     rural_male_net_enrolment_rate_primary_level__age_5_9___excluding_katchi_class_ = Column(Integer)
#     rural_female_net_enrolment_rate_primary_level__age_5_9___excluding_katchi_class_ = Column(Integer)
#     total_rural_net_enrolment_rate_primary_level__age_5_9___excluding_katchi_class_ = Column(Integer)
#     total_male_net_enrolment_rate_primary_level__age_5_9___excluding_katchi_class_ = Column(Integer)
#     total_female_net_enrolment_rate_primary_level__age_5_9___excluding_katchi_class_ = Column(Integer)
#     total_net_enrolment_rate_primary_level__age_5_9___excluding_katchi_class_ = Column(Integer)
#     urban_male_net_enrolment_rate_primary_level__age_6_10___excluding_katchi_class_ = Column(Integer)
#     urban_female_net_enrolment_rate_primary_level__age_6_10___excluding_katchi_class_ = Column(Integer)
#     total_urban_net_enrolment_rate_primary_level__age_6_10___excluding_katchi_class_ = Column(Integer)
#     rural_male_net_enrolment_rate_primary_level__age_6_10___excluding_katchi_class_ = Column(Integer)
#     rural_female_net_enrolment_rate_primary_level__age_6_10___excluding_katchi_class_ = Column(Integer)
#     total_rural_net_enrolment_rate_primary_level__age_6_10___excluding_katchi_class_ = Column(Integer)
#     total_male_net_enrolment_rate_primary_level__age_6_10___excluding_katchi_class_ = Column(Integer)
#     total_female_net_enrolment_rate_primary_level__age_6_10___excluding_katchi_class_ = Column(Integer)
#     total_net_enrolment_rate_primary_level__age_6_10___excluding_katchi_class_ = Column(Integer)
#     urban_male_net_enrolment_rate_primary_level__age_4_9___including_katchi_class_ = Column(Integer)
#     urban_female_net_enrolment_rate_primary_level__age_4_9___including_katchi_class_ = Column(Integer)
#     total_urban_net_enrolment_rate_primary_level__age_4_9___including_katchi_class_ = Column(Integer)
#     rural_male_net_enrolment_rate_primary_level__age_4_9___including_katchi_class_ = Column(Integer)
#     rural_female_net_enrolment_rate_primary_level__age_4_9___including_katchi_class_ = Column(Integer)
#     total_rural_net_enrolment_rate_primary_level__age_4_9___including_katchi_class_ = Column(Integer)
#     total_male_net_enrolment_rate_primary_level__age_4_9___including_katchi_class_ = Column(Integer)
#     total_female_net_enrolment_rate_primary_level__age_4_9___including_katchi_class_ = Column(Integer)
#     total_net_enrolment_rate_primary_level__age_4_9___including_katchi_class_ = Column(Integer)
#     urban_male_net_enrolment_rate_in_government_primary_schools__age_5_9_excluding_katchi_class_ = Column(Integer)
#     urban_female_net_enrolment_rate_in_government_primary_schools__age_5_9___excluding_katchi_class_ = Column(Integer)
#     total_urban_net_enrolment_rate_in_government_primary_schools__age_5_9___excluding_katchi_class_ = Column(Integer)
#     rural_male_net_enrolment_rate_in_government_primary_schools__age_5_9___excluding_katchi_class_ = Column(Integer)
#     rural_female_net_enrolment_rate_in_government_primary_schools__age_5_9___excluding_katchi_class_ = Column(Integer)
#     total_rural_net_enrolment_rate_in_government_primary_schools__age_5_9___excluding_katchi_class_ = Column(Integer)
#     total_male_net_enrolment_rate_in_government_primary_schools__age_5_9___excluding_katchi_class_ = Column(Integer)
#     total_female_net_enrolment_rate_in_government_primary_schools__age_5_9___excluding_katchi_class_ = Column(Integer)
#     total_net_enrolment_rate_in_government_primary_schools__age_5_9___excluding_katchi_class_ = Column(Integer)
#     urban_male_primary_level_enrolment_in_government_schools_a_percentage_of_total_enrolment__excluding_katchi_class_ = Column(Integer)
#     urban_female_primary_level_enrolment_in_government_schools_a_percentage_of_total_enrolment__excluding_katchi_class_ = Column(Integer)
#     total_urban_primary_level_enrolment_in_government_schools_a_percentage_of_total_enrolment__excluding_katchi_class_ = Column(Integer)
#     rural_male_primary_level_enrolment_in_government_schools_a_percentage_of_total_enrolment__excluding_katchi_class_ = Column(Integer)
#     rural_female_primary_level_enrolment_in_government_schools_a_percentage_of_total_enrolment__excluding_katchi_class_ = Column(Integer)
#     total_rural_primary_level_enrolment_in_government_schools_a_percentage_of_total_enrolment__excluding_katchi_class_ = Column(Integer)
#     total_male_primary_level_enrolment_in_government_schools_a_percentage_of_total_enrolment__excluding_katchi_class_ = Column(Integer)
#     total_female_primary_level_enrolment_in_government_schools_a_percentage_of_total_enrolment__excluding_katchi_class_ = Column(Integer)
#     total_primary_level_enrolment_in_government_schools_a_percentage_of_total_primary_enrolment__excluding_katchi_class_ = Column(Integer)
#     urban_male_primary_level_enrolment_in_government_schools_a_percentage_of_total_primary_enrolment__including_katchi_class_ = Column(Integer)
#     urban_female_primary_level_enrolment_in_government_schools_a_percentage_of_total_primary_enrolment__including_katchi_class_ = Column(Integer)
#     total_urban_primary_level_enrolment_in_government_schools_a_percentage_of_total_primary_enrolment__including_katchi_class_ = Column(Integer)
#     rural_male_primary_level_enrolment_in_government_schools_a_percentage_of_total_primary_enrolment__including_katchi_class_ = Column(Integer)
#     rural_female_primary_level_enrolment_in_government_schools_a_percentage_of_total_primary_enrolment__including_katchi_class_ = Column(Integer)
#     total_rural_primary_level_enrolment_in_government_schools_a_percentage_of_total_primary_enrolment__including_katchi_class_ = Column(Integer)
#     total_male_primary_level_enrolment_in_government_schools_a_percentage_of_total_primary_enrolment__including_katchi_class_ = Column(Integer)
#     total_female_primary_level_enrolment_in_government_schools_a_percentage_of_total_primary_enrolment__including_katchi_class_ = Column(Integer)
#     total_primary_level_enrolment_in_government_schools_a_percentage_of_total_primary_enrolment__including_katchi_class_ = Column(Integer)
#     urban_male_gross_enrolment_rate__middle_level__age_10_12_ = Column(Integer)
#     urban_female_gross_enrolment_rate_middle_level__age_10_12_ = Column(Integer)
#     total_urban_gross_enrolment_rate_middle_level__age_10_12_ = Column(Integer)
#     rural_male_gross_enrolment_rate_middle_level__age_10_12_ = Column(Integer)
#     rural_female_gross_enrolment_rate_middle_level__age_10_12_ = Column(Integer)
#     total_rural_gross_enrolment_rate_middle_level__age_10_12_ = Column(Integer)
#     total_male_gross_enrolment_rate_middle_level__age_10_12_ = Column(Integer)
#     total_female_gross_enrolment_rate_middle_level__age_10_12_ = Column(Integer)
#     total_gross_enrolment_rate_middle_level__age_10_12_ = Column(Integer)
#     urban_male_gross_enrolment_rate_middle_level__age_11_13_ = Column(Integer)
#     urban_female_gross_enrolment_rate_middle_level__age_11_13_ = Column(Integer)
#     total_urban_gross_enrolment_rate_middle_level__age_11_13_ = Column(Integer)
#     rural_male_gross_enrolment_rate_middle_level__age_11_13_ = Column(Integer)
#     rural_female_gross_enrolment_rate_middle_level__age_11_13_ = Column(Integer)
#     total_rural_gross_enrolment_rate_middle_level__age_11_13_ = Column(Integer)
#     total_male_gross_enrolment_rate_middle_level__age_11_13_ = Column(Integer)
#     total_female_gross_enrolment_rate_middle_level__age_11_13_ = Column(Integer)
#     total_gross_enrolment_rate_middle_level__age_11_13_ = Column(Integer)
#     urban_male_net_enrolment_rate_middle_level__age_10_12_ = Column(Integer)
#     urban_female_net_enrolment_rate_middle_level__age_10_12_ = Column(Integer)
#     total_urban_net_enrolment_rate_middle_level__age_10_12_ = Column(Integer)
#     rural_male_net_enrolment_rate_middle_level__age_10_12_ = Column(Integer)
#     rural_female_net_enrolment_rate_middle_level__age_10_12_ = Column(Integer)
#     total_rural_net_enrolment_rate_middle_level__age_10_12_ = Column(Integer)
#     total_male_net_enrolment_rate_middle_level__age_10_12_ = Column(Integer)
#     total_female_net_enrolment_rate_middle_level__age_10_12_ = Column(Integer)
#     total_net_enrolment_rate_middle_level__age_10_12_ = Column(Integer)
#     urban_male_net_enrolment_rate_middle_level__age_11_13_ = Column(Integer)
#     urban_female_net_enrolment_rate_middle_level__age_11_13_ = Column(Integer)
#     total_urban_net_enrolment_rate_middle_level__age_11_13_ = Column(Integer)
#     rural_male_net_enrolment_rate_middle_level__age_11_13_ = Column(Integer)
#     rural_female_net_enrolment_rate_middle_level__age_11_13_ = Column(Integer)
#     total_rural_net_enrolment_rate_at_the_middle_level__age_11_13_ = Column(Integer)
#     total_male_net_enrolment_rate__middle_level__age_11_13_ = Column(Integer)
#     total_female_net_enrolment_rate_middle_level__age_11_13_ = Column(Integer)
#     total_net_enrolment_rate_middle_level__age_11_13_ = Column(Integer)
#     urban_male_gross_enrolment_rate_matric_level__age_13_14_ = Column(Integer)
#     urban_female_gross_enrolment_rate_matric_level__age_13_14_ = Column(Integer)
#     total_urban_gross_enrolment_rate_matric_level__age_13_14_ = Column(Integer)
#     rural_male_gross_enrolment_rate_matric_level__age_13_14_ = Column(Integer)
#     rural_female_gross_enrolment_rate_matric_level__age_13_14_ = Column(Integer)
#     total_rural_gross_enrolment_rate_matric_level__age_13_14_ = Column(Integer)
#     total_male_gross_enrolment_rate_matric_level__age_13_14_ = Column(Integer)
#     total_female_gross_enrolment_rate_matric_level__age_13_14_ = Column(Integer)
#     total_gross_enrolment_rate_matric_level__age_13_14_ = Column(Integer)
#     urban_male_gross_enrolment_rate_matric_level__age_14_15_ = Column(Integer)
#     urban_female_gross_enrolment_rate_matric_level__age_14_15_ = Column(Integer)
#     total_urban_gross_enrolment_rate_matric_level__age_14_15_ = Column(Integer)
#     rural_male_gross_enrolment_rate_matric_level__age_14_15_ = Column(Integer)
#     rural_female_gross_enrolment_rate_matric_level__age_14_15_ = Column(Integer)
#     total_rural_gross_enrolment_rate_matric_level__age_14_15_ = Column(Integer)
#     total_male_gross_enrolment_rate_matric_level__age_14_15_ = Column(Integer)
#     total_female_gross_enrolment_rate_matric_level__age_14_15_ = Column(Integer)
#     total_gross_enrolment_rate_matric_level__age_14_15_ = Column(Integer)
#     urban_male_net_enrolment_rate_matric_level__age_13_14_ = Column(Integer)
#     urban_female_net_enrolment_rate_matric_level__age_13_14_ = Column(Integer)
#     total_urban_net_enrolment_rate_matric_level__age_13_14_ = Column(Integer)
#     rural_male_net_enrolment_rate_matric_level__age_13_14_ = Column(Integer)
#     rural_female_net_enrolment_rate_matric_level__age_13_14_ = Column(Integer)
#     total_rural_net_enrolment_rate_matric_level__age_13_14_ = Column(Integer)
#     total_male_net_enrolment_rate_matric_level__age_13_14_ = Column(Integer)
#     total_female_net_enrolment_rate_matric_level__age_13_14_ = Column(Integer)
#     total_net_enrolment_rate_matric_level__age_13_14_ = Column(Integer)
#     urban_male_net_enrolment_rate_matric_level__age_14__15_ = Column(Integer)
#     urban_female_net_enrolment_rate_matric_level__age_14__15_ = Column(Integer)
#     total_urban_net_enrolment_rate_matric_level__age_14__15_ = Column(Integer)
#     rural_male_net_enrolment_rate_matric_level__age_14__15_ = Column(Integer)
#     rural_female_net_enrolment_rate_matric_level__age_14__15_ = Column(Integer)
#     total_rural_net_enrolment_rate_matric_level__age_14__15_ = Column(Integer)
#     total_male_net_enrolment_rate_matric_level__age_14__15_ = Column(Integer)
#     total_female_net_enrolment_rate_matric_level__age_14__15_ = Column(Integer)
#     total_net_enrolment_rate_matric_level__age_14__15_ = Column(Integer)
#     urban_male_literacy_population_10_years_and_older = Column(Integer)
#     urban_female_literacy_population_10_years_and_older = Column(Integer)
#     total_urban_literacy_population_10_years_and_older = Column(Integer)
#     rural_male_literacy_population_10_years_and_older = Column(Integer)
#     rural_female_literacy_population_10_years_and_older = Column(Integer)
#     total_rural_literacy_population_10_years_and_older = Column(Integer)
#     total_male_literacy_population_10_years_and_older = Column(Integer)
#     total_female_literacy_population_10_years_and_older = Column(Integer)
#     total_literacy_population_10_years_and_older = Column(Integer)
#     urban_male_adult_literacy_population_15_years_and_older = Column(Integer)
#     urban_female_adult_literacy_population_15_years_and_older = Column(Integer)
#     total_urban_adult_literacy_population_15_years_and_older = Column(Integer)
#     rural_male_adult_literacy_population_15_years_and_older = Column(Integer)
#     rural_female_adult_literacy_population_15_years_and_older = Column(Integer)
#     total_rural_adult_literacy_population_15_years_and_older = Column(Integer)
#     total_male_adult_literacy_population_15_years_and_older = Column(Integer)
#     total_female_adult_literacy_population_15_years_and_older = Column(Integer)
#     total_adult_literacy_population_15_years_and_older = Column(Integer)
#     urban_female_enrolment_as_percentage_of_total_primary_level_enrolment__excluding_katchi_class_ = Column(Integer)
#     rural_female_enrolment_as_percentage_of_total_primary_level_enrolment__excluding_katchi_class_ = Column(Integer)
#     total_female_enrolment_as_percentage_of_total_primary_level_enrolment__excluding_katchi_class_ = Column(Integer)
#     urban_female_enrolment_as_percentage_of_total_primary_level_enrolment__including_katchi_class_ = Column(Integer)
#     rural_female_enrolment_as_percentage_of_total_primary_level_enrolment__including_katchi_class_ = Column(Integer)
#     total_female_enrolment_as_percentage_of_total_primary_level_enrolment__including_katchi_class_ = Column(Integer)
#     percentage_of_urban_male_children_10_18_years_that_left_school_before_completing_primary_level = Column(Integer)
#     percentage_of_urban_female_children_10_18_years_that_left_school_before_completing_primary_level = Column(Integer)
#     percentage_of_total_urban_children_10_18_years_that_left_school_before_completing_primary_level = Column(Integer)
#     percentage_of_rural_male_children_10_18_years_that_left_school_before_completing_primary_level = Column(Integer)
#     percentage_of_rural_female_children_10_18_years_that_left_school_before_completing_primary_level = Column(Integer)
#     percentage_of_total_rural_children_10_18_years_that_left_school_before_completing_primary_level = Column(Integer)
#     percentage_of_male_children_10_18_years_that_left_school_before_completing_primary_level = Column(Integer)
#     percentage_of_female_children_10_18_years_that_left_school_before_completing_primary_level = Column(Integer)
#     percentage_of_total_children_10_18_years_that_left_school_before_completing_primary_level = Column(Integer)
#     urban_male_enrolment_in_katchi_class_as_a_percentage_of_total_enrolment_in_katchi_and_class_one = Column(Integer)
#     urban_female_enrolment_in_katchi_class_as_a_percentage_of_total_enrolment_in_katchi_and_class_one = Column(Integer)
#     total_urban_enrolment_in_katchi_class_as_a_percentage_of_total_enrolment_in_katchi_and_class_one = Column(Integer)
#     rural_male_enrolment_in_katchi_class_as_a_percentage_of_total_enrolment_in_katchi_and_class_one = Column(Integer)
#     rural_female_enrolment_in_katchi_class_as_a_percentage_of_total_enrolment_in_katchi_and_class_one = Column(Integer)
#     total_rural_enrolment_in_katchi_class_as_a_percentage_of_total_enrolment_in_katchi_and_class_one = Column(Integer)
#     total_male_enrolment_in_katchi_class_as_a_percentage_of_total_enrolment_in_katchi_and_class_one = Column(Integer)
#     total_female_enrolment_in_katchi_class_as_a_percentage_of_total_enrolment_in_katchi_and_class_one = Column(Integer)
#     total_enrolment_in_katchi_class_as_a_percentage_of_total_enrolment_in_katchi_and_class_one = Column(Integer)
#     urban_male_enrolment_in_katchi_class_as_percentage_of_total_primary_enrolment = Column(Integer)
#     urban_female_enrolment_in_katchi_class_as_percentage_of_total_primary_enrolment = Column(Integer)
#     total_urban_enrolment_in_katchi_class_as_percentage_of_total_primary_enrolment = Column(Integer)
#     rural_male_enrolment_in_katchi_class_as_percentage_of_total_primary_enrolment = Column(Integer)
#     rural_female_enrolment_in_katchi_class_as_percentage_of_total_primary_enrolment = Column(Integer)
#     total_rural_enrolment_in_katchi_class_as_percentage_of_total_primary_enrolment = Column(Integer)
#     total_male_enrolment_in_katchi_class_as_percentage_of_total_primary_enrolment = Column(Integer)
#     total_female_enrolment_in_katchi_class_as_percentage_of_total_primary_enrolment = Column(Integer)
#     total_enrolment_in_katchi_class_as_percentage_of_total_primary_enrolment = Column(Integer)
#
# print Base.metadata.create_all(engine)
#
# Session = sessionmaker(bind=engine)
# Session.configure(bind=engine)
# session = Session()
#
# od = EducationData(country='Pakistan')
# session.add(od)
# session.commit()