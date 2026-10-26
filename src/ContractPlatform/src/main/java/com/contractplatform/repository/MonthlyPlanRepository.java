package com.contractplatform.repository;


import com.contractplatform.domain.models.MonthlyPlan;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface MonthlyPlanRepository extends JpaRepository<MonthlyPlan, Long> {
}
