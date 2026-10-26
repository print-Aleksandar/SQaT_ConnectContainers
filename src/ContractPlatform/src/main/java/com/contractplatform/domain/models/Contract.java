package com.contractplatform.domain.models;

import jakarta.persistence.*;
import java.time.OffsetDateTime;

@Entity
@Table(name = "contracts")
public class Contract {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "user_id", nullable = false,
            foreignKey = @ForeignKey(name = "contracts_user_id_fkey"))
    private Client client;

    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "plan_id", nullable = false,
            foreignKey = @ForeignKey(name = "contracts_plan_id_fkey"))
    private MonthlyPlan plan;

    @Column(name = "api_key_hash", nullable = false, unique = true, length = 64)
    private String apiKeyHash;

    @Column(name = "platform_name", nullable = false, length = 100)
    private String platformName;

    @Column(name = "player1_representation", nullable = false, length = 1)
    private String player1Representation;

    @Column(name = "player2_representation", nullable = false, length = 1)
    private String player2Representation;

    @Column(name = "empty_representation", nullable = false, length = 1)
    private String emptyRepresentation;

    @Column(name = "start_timestamp", nullable = false, updatable = false)
    private OffsetDateTime startTimestamp;

    @Column(name = "end_timestamp")
    private OffsetDateTime endTimestamp;

    @Column(name = "calls_count", nullable = false)
    private Integer callsCount = 0;

    @Column(name = "is_active", nullable = false)
    private Boolean isActive = true;

    @PrePersist
    protected void onCreate() {
        if (startTimestamp == null) {
            startTimestamp = OffsetDateTime.now();
        }
        if (callsCount == null) {
            callsCount = 0;
        }
        if (isActive == null) {
            isActive = true;
        }
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public Client getClient() { return client; }
    public void setClient(Client client) { this.client = client; }

    public MonthlyPlan getPlan() { return plan; }
    public void setPlan(MonthlyPlan plan) { this.plan = plan; }

    public String getApiKeyHash() { return apiKeyHash; }
    public void setApiKeyHash(String apiKeyHash) { this.apiKeyHash = apiKeyHash; }

    public String getPlatformName() { return platformName; }
    public void setPlatformName(String platformName) { this.platformName = platformName; }

    public String getPlayer1Representation() { return player1Representation; }
    public void setPlayer1Representation(String player1Representation) { this.player1Representation = player1Representation; }

    public String getPlayer2Representation() { return player2Representation; }
    public void setPlayer2Representation(String player2Representation) { this.player2Representation = player2Representation; }

    public String getEmptyRepresentation() { return emptyRepresentation; }
    public void setEmptyRepresentation(String emptyRepresentation) { this.emptyRepresentation = emptyRepresentation; }

    public OffsetDateTime getStartTimestamp() { return startTimestamp; }
    public void setStartTimestamp(OffsetDateTime startTimestamp) { this.startTimestamp = startTimestamp; }

    public OffsetDateTime getEndTimestamp() { return endTimestamp; }
    public void setEndTimestamp(OffsetDateTime endTimestamp) { this.endTimestamp = endTimestamp; }

    public Integer getCallsCount() { return callsCount; }
    public void setCallsCount(Integer callsCount) { this.callsCount = callsCount; }

    public Boolean getIsActive() { return isActive; }
    public void setIsActive(Boolean isActive) { this.isActive = isActive; }
}
