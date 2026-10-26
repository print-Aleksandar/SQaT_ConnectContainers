package com.contractplatform.repository;

import com.contractplatform.domain.models.MonthlyPlan;
import lombok.RequiredArgsConstructor;
import org.jspecify.annotations.NonNull;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
public class DataInitializer implements CommandLineRunner {

    private final MonthlyPlanRepository monthlyPlanRepository;

    @Override
    public void run(String @NonNull ... args) {
        if (monthlyPlanRepository.count() == 0) {
            monthlyPlanRepository.save(new MonthlyPlan("Developer Free Plan", 5000));
            monthlyPlanRepository.save(new MonthlyPlan("Developer Pro Plan", 50000));
            monthlyPlanRepository.save(new MonthlyPlan("Developer Expert Plan", 500000));
        }
    }
}